from tortoise import Model, fields
from pydantic import BaseModel
from datetime import _Datetime

class User(Model):
    id= fields.InteField(pk= True, index=True)
    username = fields.CharField(max_length=20, null=False, Unique = True)
    email=fields.CharField(max_length=200, null=False, Unique = True)
    password=fields.CharField(max_length=100, null=False)
    is_verified=fields.BooleanField(default=False)
    join_data=fields.DatetimeField(default=)



