from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

ANIO_MINIMO = 1450


class LibroBase(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    autor: str = Field(min_length=1, max_length=120)
    isbn: str = Field(min_length=10, max_length=13)
    anio_publicacion: int = Field(ge=ANIO_MINIMO, le=date.today().year)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    disponible: bool = Field(default=True)

    @field_validator("isbn")
    @classmethod
    def isbn_solo_digitos(cls, valor: str) -> str:
        limpio = valor.replace("-", "").strip()
        if not limpio.isdigit():
            raise ValueError("El ISBN debe contener solo dígitos (se permiten guiones)")
        if len(limpio) not in (10, 13):
            raise ValueError("El ISBN debe tener 10 u 13 dígitos")
        return limpio

    @field_validator("titulo", "autor")
    @classmethod
    def sin_espacios_extremos(cls, valor: str) -> str:
        limpio = valor.strip()
        if not limpio:
            raise ValueError("Este campo no puede estar vacío")
        return limpio


class LibroCreate(LibroBase):
    pass


class LibroUpdate(LibroBase):
    pass


class LibroRead(LibroBase):
    id: UUID

    model_config = {"from_attributes": True}