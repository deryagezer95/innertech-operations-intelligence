from data_loader import load_orders
from risk_engine import find_delay_risks
from priority_engine import calculate_priority
from priority_engine import calculate_delay
from delivery_engine import calculate_days_until_delivery

orders = load_orders()
upcoming_deliveries = 0
high_priority = 0
total_orders = len(orders)
risks = find_delay_risks(orders)
no_risk = total_orders - len(risks)
print("Total Orders:", total_orders)
print("No Risk:", no_risk)

print("Delay Risks:")
for order in orders:
    days_until_delivery = calculate_days_until_delivery(order)
    if 0 <= days_until_delivery <= 3:
        upcoming_deliveries += 1
print("Upcoming Deliveries:", upcoming_deliveries)

for order in risks:
    priority = calculate_priority(order)
    if priority == "HIGH":
       high_priority += 1
    days_late = calculate_delay(order)
    days_until_delivery = calculate_days_until_delivery(order)

    print(
        order.order_id,
        "-",
        order.customer,
        "→ DELAY RISK",
        "Priority:", priority ,
        "Days Late:", days_late
    )
print("High Priority:", high_priority)