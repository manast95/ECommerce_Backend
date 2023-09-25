from pydantic import BaseModel
from datetime import datetime
from typing import List

class User(BaseModel):
    name: str
    price: float
    quantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zipcode: int

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int

class Order(BaseModel):
    timestamp: datetime
    items: List[OrderItem] = []
    total_amount: float
    address: UserAddress
