import datetime
from sqlalchemy.orm import Session
from db.engine import engine
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ItemHistoryLot


def add_history_lot(
        amount: int, time: datetime.datetime, price: int,
        region: str, item: str) -> None:
    with Session(bind=engine) as session:
        session.add(ItemHistoryLot(
            amount=amount, time=time, price=price,
            region=region, item=item))
        session.commit()

async def add_history_lot_async(
        amount: int, time: datetime.datetime, price: int,
        region: str, item: str) -> None:
    async_session = AsyncSession(bind=engine)
    async_session.add(ItemHistoryLot(
        amount=amount, time=time, price=price,
        region=region, item=item))
    await async_session.commit()
