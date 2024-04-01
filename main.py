from fastapi import FastAPI;
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from models import *
from authentication import (get_hashed_password)
#signals
from tortoise.signals import post_save
from typing import List,Optional,Type
from tortoise import BaseDBAsyncClient



app= FastAPI()

@post_save(User)
async def create_business(
    sender : "Type[User]",
    instance : User,
    created:bool,
    using_db :"Optional[BaseDBAsyncClient]",
    update_fields : List[str]
) -> None :
    if created:


@app.post("/registration")
async def user_registrations(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"]=get_hashed_password(user_info["password"])
    user_obj=await User.create(**user_info)
    new_user=await user_pydantic.from_tortoise_orm(user_obj)
    return{
        "status":"ok",
        "data" :f"Hello {new_user.username}, tthanks for choosing our services.pls check ur mail and click on the link to confirm ur registration."
    }

@app.get("/")
def index():
    return {"Message":"hello world"}


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True

)