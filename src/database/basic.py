import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


class Base(DeclarativeBase):
    id: Mapped[int_pk]

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = [f'{col}={getattr(self, col)}' for indx, col in enumerate(self.__table__.columns.keys()) if
                col in self.repr_cols or indx < self.repr_cols_num]
        return f'<{self.__class__.__name__} {','.join(cols)}>'