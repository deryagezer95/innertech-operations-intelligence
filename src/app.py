from data_loader import load_orders
from risk_engine import find_delay_risks
from priority_engine import calculate_priority
from priority_engine import calculate_delay

orders = load_orders()

risks = find_delay_risks(orders)

print("Delay Risks:")

for order in risks:
    priority = calculate_priority(order)
    days_late = calculate_delay(order)

    print(
        order.order_id,
        "-",
        order.customer,
        "→ DELAY RISK",
        "Priority:", priority ,
        "Days Late:", days_late
    )