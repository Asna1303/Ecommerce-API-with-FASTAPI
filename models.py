from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime

class User(Model):
    id= fields.InteField(pk= True, index=True)
    username = fields.CharField(max_length=20, null=False, Unique = True)
    email=fields.CharField(max_length=200, null=False, Unique = True)
    password=fields.CharField(max_length=100, null=False)
    is_verified=fields.BooleanField(default=False)
    join_data=fields.DatetimeField(default=datetime.utcnow)
    

class Business(Model):
     id= fields.InterField(pk= True, index=True)
     business_name = fields.CharField(max_length=20, null=False, Unique = True)
     city=fields.CharField(max_length=100, null=False, default="Unspecified")
     region=fields.CharField(max_length=100, null=False, default="Unspecified")
     business_description=fields.TextField(null=True)
     logo=fields.CharField(max_length=200, null=False, default="default.jpg")



