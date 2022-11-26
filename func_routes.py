from fastapi import APIRouter
from schemas import SpamModel

func_router = APIRouter(
    prefix='/func',
    tags=['function_tag']
)

@func_router.get('/')
async def hello():
    return {'message':'Hello_World'}

@app.put('/spam/{phone_no}')
async def mark_spam(phone_no:str,user:SpamModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    

