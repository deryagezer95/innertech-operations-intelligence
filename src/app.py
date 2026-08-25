from data_loader import load_orders
from risk_engine import find_delay_risks
from priority_engine import calculate_priority
from priority_engine import calculate_delay
from delivery_engine import calculate_days_until_delivery
from decision_engine import calculate_decision
from action_queue import build_action_queue

orders = load_orders()
immediate_actions, reviews, monitors, no_actions = build_action_queue(orders)
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
    priority = calculate_priority(order)
    if priority.startswith("HIGH"):
      high_priority += 1

print("Upcoming Deliveries:", upcoming_deliveries)
print("Operations:")
for order in orders:
    priority = calculate_priority(order)
    decision = calculate_decision(order)
    days_until_delivery = calculate_days_until_delivery(order)
    print(order.order_id, "-", order.customer, "| Priority:", priority, "| Days Until Delivery:", days_until_delivery, "| Decision:", decision)
print("High Priority:", high_priority)
print("ACTION QUEUE")
print("IMMEDIATE ACTION")
for order in immediate_actions:
    print(
    order.order_id,
    "-",
    order.customer,
    "| Days Late:",
    -calculate_days_until_delivery(order)
)
print("REVIEW")
for order in reviews:
    print(
    order.order_id,
    "-",
    order.customer,
    "| Days Late:",
    -calculate_days_until_delivery(order)
)
print("MONITOR")
for order in monitors:
    print(
    order.order_id,
    "-",
    order.customer,
    "|Days Until Delivery:",
    calculate_days_until_delivery(order)
)
print("NO ACTION REQUIRED")
for order in no_actions:
    print(order.order_id, "-", order.customer)
