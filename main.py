# fastapi dev main.py
from fastapi import FastAPI, HTTPException, Request, Query
from typing import Optional, Annotated
from unicodedata import name
from mobileProducts import products  # load data;

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


# This endpoint shows how to access path parameters using the function parameters
@app.get("/productlist/{id}")
def get_product(id: Optional[int]):

    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


# This endpoint shows how to access query parameters using the function parameters with default values
# http://127.0.0.1:8000/producstlist?id=4
@app.get("/producstlist")
def get_productlist(id: Optional[int] = None):

    # If ID is provided
    if id is not None:
        for product in products:
            if product["id"] == id:
                return product

        return {"message": "Product not found"}

    # If no ID provided
    return products


# This endpoint demonstrates how to access query parameters using the Request object
# http://127.0.0.1:8000/user?name=Shahzain&age=20


@app.get("/user")
def user(request: Request):
    query_params = request.query_params
    print(query_params)
    return {
        "user": f"my name is {query_params.get('name')} and i'm a software developer {query_params.get('age')} years old"
    }


# modified v2


@app.get("/userDev/")
async def read_developers(query: dict = {"name": "Shahzain", "age": 25}):
    return {
        "user Developers": f"my name is {query.get('name')} and i'm a software developer {query.get('age')} years old"
    }
