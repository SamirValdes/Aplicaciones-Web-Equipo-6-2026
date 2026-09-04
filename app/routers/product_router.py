from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.product_crud import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product,
)
from app.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate


product_router = APIRouter(prefix="/products", tags=["products"])
DbSession = Annotated[Session, Depends(get_db)]


@product_router.post(
    "", response_model=ProductResponse, status_code=status.HTTP_201_CREATED
)
def create_product_endpoint(
    product_data: ProductCreate, db: DbSession
) -> ProductResponse:
    return create_product(db, product_data)


@product_router.get("", response_model=list[ProductResponse])
def list_products(db: DbSession) -> list[ProductResponse]:
    return get_products(db)


@product_router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: DbSession) -> ProductResponse:
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )
    return product


@product_router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(
    product_id: int, product_data: ProductUpdate, db: DbSession
) -> ProductResponse:
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )
    return update_product(db, product, product_data)


@product_router.delete("/{product_id}", response_model=ProductResponse)
def delete_product_endpoint(product_id: int, db: DbSession) -> ProductResponse:
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )
    return delete_product(db, product)