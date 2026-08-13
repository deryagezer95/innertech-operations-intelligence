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

    def is_active(self) -> bool:
        return self.status != "Completed"

    def is_delayed(self) -> bool:
        return self.is_active() and self.delivery_date < date.today()


orders = [
    Order(
        order_id="ORD-001",
        customer="ABC Plastik",
        product="Ürün X",
        quantity=1000,
        delivery_date=date(2026, 8, 10),
        status="New",
    ),
    Order(
        order_id="ORD-002",
        customer="Beta Makine",
        product="Ürün Y",
        quantity=500,
        delivery_date=date(2026, 8, 20),
        status="In Progress",
    ),
    Order(
        order_id="ORD-003",
        customer="Gamma Dış Ticaret",
        product="Ürün Z",
        quantity=250,
        delivery_date=date(2026, 8, 5),
        status="Completed",
    ),
]


print("Active Orders:")

for order in orders:
    if order.is_active():
        print(order.order_id, "-", order.customer)


print("\nDelay Risk:")

for order in orders:
    if order.is_delayed():
        print(order.order_id, "-", order.customer, "→ DELAY RISK")