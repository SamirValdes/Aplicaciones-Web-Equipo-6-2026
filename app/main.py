from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.product import Product  # noqa: F401
from app.models.libro import Libro  # noqa: F401
from app.routers.product_router import product_router
from app.routers.libro_router import libro_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Products API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(libro_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "API funcionando correctamente"}