from uuid import uuid4

from sqlalchemy import ForeignKey, Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base


class  User(Base):
    """
    Модель пользователя.

    Attrs:
        id (int): Уникальный идентификатор пользователя.
        user_name (str): Имя пользователя или логин.
        user_password (str): Пароль пользователя.
        role (str): Роль пользователя (например, 'admin').
        cookies (list[Cookie]): Список cookie-токенов, связанных с пользователем.
    """
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )
    user_name: Mapped[str] = mapped_column(String, unique=True)
    user_password: Mapped[str] = mapped_column(String)

    cookies = relationship("Cookie", back_populates="user")
    functions = relationship(
        "UserFunctionsMap",
        back_populates="user",
    )


class Cookie(Base):
    """
    Модель cookie пользователя.

    Attrs:
        id (int): Уникальный идентификатор записи cookie.
        user_id (int): Внешний ключ на пользователя.
        token (str): Уникальный токен пользователя.
        user (User): Объект пользователя, которому принадлежит токен.
    """
    __tablename__ = "cookies"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    token: Mapped[str] = mapped_column(String, nullable=False)

    user = relationship("User", back_populates="cookies")


class TerminalFunctions(Base):
    __tablename__ = "terminal_functions"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )
    function_name: Mapped[str] = mapped_column(String, unique=True)
    endpoint_name: Mapped[str] = mapped_column(String, unique=True)
    module_name: Mapped[str] = mapped_column(String, nullable=True)

    users = relationship(
        "UserFunctionsMap",
        back_populates="terminal_function",
    )


class UserFunctionsMap(Base):
    """Таблица соответствий пользователей и терминальных функций."""
    __tablename__ = "user_functions_map"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    terminal_function_id: Mapped[int] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("terminal_functions.id"),
        nullable=False,
    )

    user = relationship("User", back_populates="functions")
    terminal_function = relationship("TerminalFunctions", back_populates="users")
