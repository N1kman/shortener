from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.basic import Base, created_at
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from typing import Optional


class UrlPairOrm(Base):
    __tablename__ = 'url'

    long_url: Mapped[str] = mapped_column(nullable=False)
    short_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    user: Mapped['UserOrm'] = relationship(back_populates='urls')


class UserOrm(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    urls: Mapped[Optional[list['UrlPairOrm']]] = relationship(back_populates='user')