from pydantic import BaseModel


from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    stock: int

class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    stock: int