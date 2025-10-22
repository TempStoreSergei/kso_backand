from sqlalchemy import String, Integer, ForeignKey, Table, Column, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base


class Guest(Base):
    __tablename__ = "guests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str | None] = mapped_column(String(100), nullable=True)

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="guest"
    )


# Таблица связи между транзакциями и услугами
transaction_services = Table(
    "transaction_services",
    Base.metadata,
    Column("transaction_id", Integer, ForeignKey("transactions.id"), primary_key=True),
    Column("service_id", Integer, ForeignKey("services.id"), primary_key=True),
    Column("count", Integer, default=1),  # сколько единиц услуги в этой транзакции
    Column("duration", Integer, nullable=True), # продолжительность в часах
)


transaction_fines = Table(
    "transaction_fines",
    Base.metadata,
    Column("transaction_id", Integer, ForeignKey("transactions.id"), primary_key=True),
    Column("fine_id", Integer, ForeignKey("fines.id"), primary_key=True),
    Column("count", Integer, default=1),  # сколько единиц услуги в этой транзакции
)


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    price: Mapped[int] = mapped_column(Integer)
    tax: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    is_countable: Mapped[bool] = mapped_column(Boolean, default=False)
    is_duration: Mapped[bool] = mapped_column(Boolean, default=False)
    code: Mapped[int] = mapped_column(String(50))

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        secondary=transaction_services,
        back_populates="services"
    )


class Fine(Base):
    __tablename__ = "fines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    price: Mapped[int] = mapped_column(Integer)
    type: Mapped[str] = mapped_column(String(50)) # violation_rules or damage_to_property
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    code: Mapped[int] = mapped_column(String(50))

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        secondary=transaction_fines,
        back_populates="fines"
    )


class RoomPrice(Base):
    __tablename__ = "room_prices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    building: Mapped[int] = mapped_column(Integer)
    room_type: Mapped[str] = mapped_column(String(50))
    count_days: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guest_id: Mapped[int] = mapped_column(Integer, ForeignKey("guests.id"))
    room_number: Mapped[str] = mapped_column(String(30))
    room_type: Mapped[str] = mapped_column(String(50))
    room_building: Mapped[int] = mapped_column(Integer)
    count_days: Mapped[int] = mapped_column(Integer, nullable=True)
    room_day_price: Mapped[int] = mapped_column(Integer, nullable=True)
    payment_type: Mapped[str] = mapped_column(String(50), nullable=True)

    guest: Mapped["Guest"] = relationship("Guest", back_populates="transactions")
    services: Mapped[list["Service"]] = relationship(
        "Service",
        secondary=transaction_services,
        back_populates="transactions"
    )
    fines: Mapped[list["Fine"]] = relationship(
        "Fine",
        secondary=transaction_fines,
        back_populates="transactions"
    )
