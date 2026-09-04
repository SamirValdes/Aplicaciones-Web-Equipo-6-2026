from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import libro as crud
from app.database import get_db
from app.schemas.libro import LibroCreate, LibroRead, LibroUpdate

libro_router = APIRouter(prefix="/libros", tags=["libros"])


def _obtener_o_404(db: Session, libro_id: UUID):
    libro = crud.obtener_por_id(db, libro_id)
    if libro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro


@libro_router.get("", response_model=list[LibroRead])
def listar_libros(db: Session = Depends(get_db)):
    return crud.listar(db)


@libro_router.get("/{libro_id}", response_model=LibroRead)
def obtener_libro(libro_id: UUID, db: Session = Depends(get_db)):
    return _obtener_o_404(db, libro_id)


@libro_router.post("", response_model=LibroRead, status_code=status.HTTP_201_CREATED)
def crear_libro(datos: LibroCreate, db: Session = Depends(get_db)):
    if crud.obtener_por_isbn(db, datos.isbn) is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un libro con ese ISBN")
    return crud.crear(db, datos)


@libro_router.put("/{libro_id}", response_model=LibroRead)
def actualizar_libro(libro_id: UUID, datos: LibroUpdate, db: Session = Depends(get_db)):
    libro = _obtener_o_404(db, libro_id)
    duplicado = crud.obtener_por_isbn(db, datos.isbn)
    if duplicado is not None and duplicado.id != libro_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe otro libro con ese ISBN")
    return crud.actualizar(db, libro, datos)


@libro_router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(libro_id: UUID, db: Session = Depends(get_db)):
    libro = _obtener_o_404(db, libro)
    crud.eliminar(db, libro)