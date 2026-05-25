from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_session
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])


# LISTAR TODOS OS PRODUTOS
@router.get("/")
def get_products(session: Session = Depends(get_session)):
    products = session.query(Product).all()
    return products


# BUSCAR PRODUTO POR ID
@router.get("/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return product


# CRIAR PRODUTO
@router.post("/")
def create_product(product: ProductCreate, session: Session = Depends(get_session)):

    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        stock=product.stock
    )

    session.add(new_product)
    session.commit()
    session.refresh(new_product)

    return new_product


# ATUALIZAR PRODUTO
@router.put("/{product_id}")
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    session: Session = Depends(get_session)
):

    product = session.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.category = product_data.category
    product.stock = product_data.stock

    session.commit()
    session.refresh(product)

    return product


# DELETAR PRODUTO
@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):

    product = session.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    session.delete(product)
    session.commit()

    return {"message": "Produto deletado com sucesso"}