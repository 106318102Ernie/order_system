from fastapi import APIRouter, HTTPException
from models.order_models import Order
from services.order_service import OrderService

order_router = APIRouter()


@order_router.post("/api/orders")
async def create_order(order: Order):
    order_service = OrderService()
    try:
        validated_order = order_service.process_order(order)
        return validated_order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
