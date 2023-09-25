from fastapi import APIRouter
from models.user import User, Order
from config.db import conn
from schemas.user import serializeDict, serializeList
from datetime import datetime
from bson import ObjectId

user = APIRouter()

@user.get('/product')
async def find_all_products():
    products = conn.local.user.find()
    return serializeList(products)

@user.post('/product')
async def create_product(user: User):
    new_product = User(**user.dict())
    result = conn.local.user.insert_one(new_product.dict())
    return {"message": "Product created successfully", "inserted_id": str(result.inserted_id)}

@user.put('/product/{id}')
async def update_product(id, user: User):
    conn.local.user.update_one({"_id": ObjectId(id)}, {"$set": user.dict()})
    updated_product = conn.local.user.find_one({"_id": ObjectId(id)})
    return serializeDict(updated_product)

@user.delete('/product/{id}')
async def delete_product(id):
    deleted_product = conn.local.user.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_product:
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found"}

@user.get('/order')
async def find_all_orders():
    orders = conn.local.order.find()
    return serializeList(orders)

@user.post('/order')
async def create_order(order: Order):
    order.timestamp = datetime.now()
    result = conn.local.order.insert_one(order.dict())
    return {
        "message": "Order created successfully",
        "inserted_id": str(result.inserted_id),
        "total_amount": order.total_amount
    }

@user.put('/order/{id}')
async def update_order(id, order: Order):
    conn.local.order.update_one({"_id": ObjectId(id)}, {"$set": order.dict()})
    updated_order = conn.local.order.find_one({"_id": ObjectId(id)})
    return serializeDict(updated_order)

@user.delete('/order/{id}')
async def delete_order(id):
    deleted_order = conn.local.order.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_order:
        return {"message": "Order deleted successfully"}
    else:
        return {"message": "Order not found"}
