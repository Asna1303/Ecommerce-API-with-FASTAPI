from fastapi import FastAPI;
from tortoise.contrib.fastapi import register_tortoise
from models import *

app= FastAPI()
