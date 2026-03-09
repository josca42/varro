from sqlmodel import Session, select
from sqlalchemy import update

from varro.db.crud.base import CrudBase
from varro.db.db import user_engine
from varro.db.models.model_charge import ModelCharge
from varro.db.models.user import User


class CrudModelCharge(CrudBase[ModelCharge]):
    def get_by_charge_key(self, charge_key: str) -> ModelCharge | None:
        with Session(self.engine) as session:
            stmt = select(ModelCharge).where(ModelCharge.charge_key == charge_key)
            return session.exec(stmt).one_or_none()

    def create_and_debit_balance(self, charge: ModelCharge) -> bool:
        with Session(self.engine) as session, session.begin():
            existing_stmt = select(ModelCharge.id).where(
                ModelCharge.charge_key == charge.charge_key
            )
            if session.exec(existing_stmt).one_or_none() is not None:
                return False

            session.add(charge)
            decrement_stmt = (
                update(User)
                .where(User.id == charge.user_id)
                .values(balance=User.balance - charge.amount_dkk)
                .execution_options(synchronize_session=False)
            )
            result = session.exec(decrement_stmt)
            if result.rowcount != 1:
                raise RuntimeError(f"User not found for model charge: {charge.user_id}")

        return True


model_charge = CrudModelCharge(ModelCharge, user_engine)
