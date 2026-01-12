from typing import Type, TypeVar, Generic, List, Any, Optional, Dict
from sqlmodel import SQLModel, Session, select, update

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import inspect, UniqueConstraint
from functools import cached_property
import pandas as pd


ModelType = TypeVar("ModelType", bound=SQLModel)


class CrudBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], engine):
        self.model = model
        self.engine = engine

    def get_by_id(self, pk_value: Any) -> Optional[ModelType]:
        if pk_value is None:
            return None
        with Session(self.engine) as session:
            return session.get(self.model, pk_value)

    def create(self, obj: ModelType) -> ModelType:
        with Session(self.engine) as session, session.begin():
            obj_data = obj.model_dump(exclude_unset=True)
            stmt = insert(self.model).values(**obj_data).returning(self.model)
            result = session.exec(stmt).scalar_one().model_dump()
            return self.model(**result)

    def update(self, model_obj: ModelType) -> ModelType:
        model_update = model_obj.model_dump(exclude_unset=True)
        with Session(self.engine) as session, session.begin():
            stmt = update(self.model).where(
                getattr(self.model, self._primary_key_name)
                == getattr(model_obj, self._primary_key_name)
            )
            session.exec(stmt.values(**model_update))

    def delete(self, model_obj: ModelType) -> None:
        with Session(self.engine) as session, session.begin():
            merged_obj = session.merge(model_obj)
            session.delete(merged_obj)

    def upsert(self, obj: ModelType, return_model: bool = False) -> ModelType:
        unique_cols = self._get_unique_constraints
        if not unique_cols:
            unique_cols = self._get_primary_keys
        obj_data = obj.model_dump(exclude_unset=True)
        update_data = {k: v for k, v in obj_data.items() if k not in unique_cols}

        with Session(self.engine) as session, session.begin():
            stmt = insert(self.model).values(**obj_data)
            if update_data:
                stmt = stmt.on_conflict_do_update(
                    index_elements=unique_cols,
                    set_=update_data,
                )
            else:
                stmt = stmt.on_conflict_do_nothing()
            stmt = stmt.returning(self.model)

            model_instance = session.exec(stmt).scalar_one_or_none()
            if return_model:
                if model_instance is None:
                    query_params = {k: obj_data[k] for k in unique_cols}
                    model_instance = session.exec(
                        select(self.model).filter_by(**query_params)
                    ).one_or_none()
                    if model_instance is None:
                        raise ValueError(
                            f"Model instance not found for query params: {query_params}"
                        )

                return self.model(**model_instance.model_dump())

    def get_table(self):
        with Session(self.engine) as session:
            rows = session.exec(select(self.model))
            return pd.DataFrame([row.model_dump() for row in rows])

    @cached_property
    def _primary_key_name(self) -> str:
        pks = inspect(self.model).primary_key
        if len(pks) != 1:
            raise ValueError("CrudBase only supports models with a single primary key.")
        return pks[0].name

    @cached_property
    def _get_primary_keys(self):
        return [key.name for key in inspect(self.model).primary_key]

    @cached_property
    def _get_unique_constraints(self):
        constraints = [
            c
            for c in self.model.__table__.constraints
            if isinstance(c, UniqueConstraint)
        ]
        if len(constraints) > 1:
            raise ValueError(
                f"Expected exactly one unique constraint, found {len(constraints)}"
            )
        if len(constraints) == 0:
            return []
        return [col.name for col in constraints[0].columns]
