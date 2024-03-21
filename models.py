from tortoise import Model, fields
from pydantic import BaseModel


class User(Model):
    id= fields.InteField(pk= True, index=True)
    


