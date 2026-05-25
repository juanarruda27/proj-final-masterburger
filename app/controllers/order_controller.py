from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.order_model import Order, OrderItem
from app.models.product_model import Product
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.security.security import verify_token


router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token)
):
    total = 0

    new_order = Order(
        customer_name=order.customer_name,
        status="Pendente",
        total_price=0
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")

        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para {product.name}")

        product.stock -= item.quantity
        total += product.price * item.quantity

        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(order_item)

    new_order.total_price = total
    db.commit()
    db.refresh(new_order)

    return new_order


@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return order

@router.put("/{order_id}/status")
def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    order.status = status

    db.commit()
    db.refresh(order)

    return {
        "message": "Status atualizado com sucesso",
        "order": order
    }