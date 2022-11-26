from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags=['authentication_tag']
)

@auth_router.get('/')
async def hello():
    return {'message':'Hello_World'}