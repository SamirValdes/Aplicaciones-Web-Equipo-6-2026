from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.libro import Libro
from app.schemas.libro import LibroCreate, LibroUpdate


def listar(db: Session) -> list[Libro]:
    return list(db.scalars(select(Libro).order_by(Libro.titulo)))


def obtener_por_id(db: Session, libro_id: UUID) -> Libro | None:
    return db.get(Libro, libro_id)


def obtener_por_isbn(db: Session, isbn: str) -> Libro | None:
    return db.scalars(select(Libro).where(Libro.isbn == isbn)).first()


def crear(db: Session, datos: LibroCreate) -> Libro:
    libro = Libro(**datos.model_dump())
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro


def actualizar(db: Session, libro: Libro, datos: LibroUpdate) -> Libro:
    for campo, valor in datos.model_dump().items():
        setattr(libro, campo, valor)
    db.commit()
    db.refresh(libro)
    return libro


def eliminar(db: Session, libro: Libro) -> None:
    db.delete(libro)
    db.commit()