from fastapi import FastAPI
from . import auth

app = FastAPI(title="FastAPI Auth with Azure SQL")

app.include_router(auth.router)
