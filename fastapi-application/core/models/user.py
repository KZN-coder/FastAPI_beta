from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .mixins.int_id_pk import IntIdPkMixin
from .base import Base

class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (
        UniqueConstraint("foo", "bar"),
    )