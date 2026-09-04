# Products API

API REST de productos construida con FastAPI, SQLAlchemy 2.x, Pydantic v2 y PostgreSQL.

## Instalacion

1. Crear y activar un entorno virtual:

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

2. Instalar las dependencias:

	```powershell
	pip install -r requirements.txt
	```

3. Configurar `.env` con la cadena de conexion de PostgreSQL Neon:

	```env
	DATABASE_URL=postgresql+psycopg2://usuario:password@host/database?sslmode=require
	```

4. Ejecutar la API:

	```powershell
	uvicorn app.main:app --reload
	```

## Documentacion

Con el servidor activo, abrir Swagger en:

<http://127.0.0.1:8000/docs>

La API expone el CRUD completo bajo `/products`.
