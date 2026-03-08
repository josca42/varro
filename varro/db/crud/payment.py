from sqlmodel import Session, select

from varro.db.crud.base import CrudBase
from varro.db.db import user_engine
from varro.db.models.payment import StripePayment


class CrudStripePayment(CrudBase[StripePayment]):
    def get_by_checkout_session_id(self, checkout_session_id: str) -> StripePayment | None:
        with Session(self.engine) as session:
            stmt = select(StripePayment).where(
                StripePayment.checkout_session_id == checkout_session_id
            )
            return session.exec(stmt).one_or_none()

    def get_paid_for_user_checkout(
        self,
        user_id: int,
        checkout_session_id: str,
    ) -> StripePayment | None:
        with Session(self.engine) as session:
            stmt = (
                select(StripePayment)
                .where(StripePayment.user_id == user_id)
                .where(StripePayment.checkout_session_id == checkout_session_id)
                .where(StripePayment.payment_status == "paid")
            )
            return session.exec(stmt).one_or_none()


stripe_payment = CrudStripePayment(StripePayment, user_engine)
