from fastapi import FastAPI
from auth_routes import auth_router
from func_routes import func_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(func_router)