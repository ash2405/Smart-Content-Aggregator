from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.enums.role import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    password: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )

    is_active : Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    
    role : Mapped[str] = mapped_column(
        String(250),
        default=Role.USER
    )