from pydantic import BaseModel
from typing import List


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    customer_name: str
    items: List[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_price: float
    status: str
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True