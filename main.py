from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

API_KEY = os.getenv("MY_SECRET_KEY", "default_dev_key")

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500}
]

orders = []

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong!"}
    )

# Root
@app.get("/")
def home():
    return {"message": "API is running"}

# Get products
@app.get("/products")
def get_products():
    return products

# Create order
@app.post("/orders")
def create_order(order: dict):
    if "items" not in order:
        raise HTTPException(status_code=400, detail="Invalid order")

    new_order = {
        "id": len(orders) + 1,
        "items": order["items"]
    }

    orders.append(new_order)
    return new_order

# Get orders
@app.get("/orders")
def get_orders():
    return orders
