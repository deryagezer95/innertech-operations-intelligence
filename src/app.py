from data_loader import load_orders
from risk_engine import find_delay_risks


orders = load_orders()

risks = find_delay_risks(orders)

print("Delay Risks:")

for order in risks:
    print(
        order.order_id,
        "-",
        order.customer,
        "→ DELAY RISK"
    )