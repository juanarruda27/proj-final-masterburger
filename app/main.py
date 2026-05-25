from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import create_db_and_tables

from app.controllers.product_controller import router as product_router
from app.controllers.order_controller import router as order_router
from app.controllers.user_controller import router as user_router
from app.controllers.auth_controller import router as auth_router

from app.models import product_model
from app.models import order_model
from app.models import user_model


app = FastAPI(
    title="Master Burger API",
    description="Sistema de hamburgueria com FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(product_router)
app.include_router(order_router)
app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Burger System API funcionando"}