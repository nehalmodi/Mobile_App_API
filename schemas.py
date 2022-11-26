from pydantic import BaseModel
from typing import Optional

class RegisterModel(BaseModel):
    phone_no:str
    name:str
    password:str
    email: Optional[str]
    

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'phone_no':'0000000000',
                'name':'abcd',
                'password': "password",     
            }
        }



class Settings(BaseModel):
    authjwt_secret_key:str = '4adc1f00d3179d00fd5ff7a0222b6e8c03889e971e9a20fcb287945bef1de1a5'

class LoginModel(BaseModel):
    username:str
    password:str

class ContactModel(BaseModel):
    phone_no:str
    name:str
    email: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'phone_no':'0000000000',
                'name':'abcd' 
            }
        }

class SpamModel(BaseModel):
    phone_no:str

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'phone_no':'0000000000',
            }
        }