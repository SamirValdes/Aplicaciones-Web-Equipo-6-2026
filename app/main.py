from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product  # noqa: F401
from app.routers.product_router import product_router
from src.api.estudiante import router as estudiantes_router
from src.database.database import Base as StudentBase, engine as student_engine
from src.entities.estudiante import Estudiante  # noqa: F401

Base.metadata.create_all(bind=engine)
StudentBase.metadata.create_all(bind=student_engine)

app = FastAPI(title="Products API", version="1.0.0")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o el dominio de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_router)
app.include_router(estudiantes_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "API funcionando correctamente"}