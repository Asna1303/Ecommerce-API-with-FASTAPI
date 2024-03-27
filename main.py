from fastapi import FastAPI;
from tortoise.contrib.fastapi import register_tortoise
from models import *

app= FastAPI()


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    models={"models": ["models"]}
    generate_schemas=True,
    
)