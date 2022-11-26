from fastapi import APIRouter,status,Depends
from pydantic import BaseModel
from database import Session,engine
from schemas import RegisterModel,LoginModel,ContactModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(
    prefix='/auth',
    tags=['authentication_tag']
)

session = Session(bind=engine)

@auth_router.get('/')
async def hello():
    return {'message':'Hello_World'}


@auth_router.post('/register')
async def register(user:RegisterModel,status_code=status.HTTP_201_CREATED):
    if user.phone_no=="" or user.name=="" or user.password=="" :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone no. can't be null"
        )

    db_phone = session.query(User).filter(User.phone_no==user.phone_no).first()

    if db_phone is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone numbr already exist"
        )
    
    new_user = User(
        phone_no=user.phone_no,
        name=user.name,
        email=user.email,
        password=generate_password_hash(user.password)
    )

    session.add(new_user)
    session.commit()

    return new_user


@auth_router.get('/login',status_code=200)
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    db_phone = session.query(User).filter(User.phone_no==user.phone_no).first
    
    if db_phone and check_password_hash(db_phone.password, user.password):
        access_token = Authorize.create_access_token(subject=db_phone.phone_no)
        refresh_token = Authorize.create_refresh_token(subject=db_phone.phone_no)

        response = {
            "access" : access_token,
            "refresh" : refresh_token
        }

        return jsonable_encoder(response)

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid phone_no or password"
        )

@auth_router.get("/refresh")
async def refresh_token(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please provide a valid refresh token"
            )

    current_user = Authorize.get_jwt_subject()

    access_token = Authorize.create_access_token(subject=current_user)

    return jsonable_encoder({"access":access_token})


@auth_router.post("/contacts",status_code=status.HTTP_201_CREATED)
async def add_to_contact(contact:ContactModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
        

    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
            )
    
    current_user_phone = Authorize.get_jwt_subject()

    user_phone = session.query(User).filter(User.phone_no==current_user).first()

    new_contact = Contact(
        phone_no=contact.phone_no,
        name=contact.name
        
    )

    new_contact.user_phone = user_phone

    session.add(new_contact)

    session.commit()

    response = {
        "phone_no":new_contact.phone_no,
        "name":new_contact.name,
    }

    return jsonable_encoder(response)
