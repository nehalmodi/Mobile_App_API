from fastapi import APIRouter

func_router = APIRouter(
    prefix='/func',
    tags=['function_tag']
)

@func_router.get('/')
async def hello():
    return {'message':'Hello_World'}