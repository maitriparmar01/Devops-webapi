from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    description: str