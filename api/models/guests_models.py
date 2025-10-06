from sqlalchemy import String, Integer, Date, ForeignKey, Table, Column
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
)


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Integer)
    tax: Mapped[int] = mapped_column(Integer)

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        secondary=transaction_services,
        back_populates="services"
    )


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="room"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guest_id: Mapped[int] = mapped_column(Integer, ForeignKey("guests.id"))
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id"))
    check_in: Mapped[Date | None] = mapped_column(Date, nullable=True)
    check_out: Mapped[Date | None] = mapped_column(Date, nullable=True)
    payment_type: Mapped[str | None] = mapped_column(String(50), nullable=True)

    room: Mapped["Room"] = relationship("Room", back_populates="transactions")
    guest: Mapped["Guest"] = relationship("Guest", back_populates="transactions")
    services: Mapped[list["Service"]] = relationship(
        "Service",
        secondary=transaction_services,
        back_populates="transactions"
    )
