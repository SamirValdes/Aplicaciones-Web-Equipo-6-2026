from uuid import UUID, uuid4

from sqlalchemy import Boolean, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    autor: Mapped[str] = mapped_column(String(120), nullable=False)
    isbn: Mapped[str] = mapped_column(String(13), unique=True, nullable=False, index=True)
    anio_publicacion: Mapped[int] = mapped_column(Integer, nullable=False)
    precio: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)