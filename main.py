# fastapi dev main.py
from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from unicodedata import name
from mobileProducts import products

app = FastAPI()


@app.get("/")
def home():
    return "Well this is fastapi Endpoint"


@app.get("/info")
def information():
    return (
        "this is APP information about the fastapi how to use and which app route info "
    )


@app.get("/userinfo")
def get_user(user_id: int):
    return {"user_id": user_id}


# This endpoint shows how to access query parameters using the function parameters
@app.get("/search")
def search(name: str):
    return {"name": name}


@app.get("/product")
def get_product(limit: int, category: Optional[str] = None):
    return {"category": category, "limit": limit}
