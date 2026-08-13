from dataclasses import dataclass
from datetime import date


@dataclass
class Order:
    order_id: str
    customer: str
    product: str
    quantity: int
    delivery_date: date
    status: str