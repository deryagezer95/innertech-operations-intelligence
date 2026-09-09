from data_loader import load_orders
from priority_engine import calculate_priority
from delivery_engine import calculate_days_until_delivery
from decision_engine import calculate_decision
from action_queue import build_action_queue

from operations_metrics import (
    calculate_total_orders,
    calculate_no_risk,
    calculate_upcoming_deliveries,
    calculate_high_priority_orders
)


orders = load_orders()

immediate_actions, reviews, monitors, no_actions = build_action_queue(orders)

total_orders = calculate_total_orders(orders)
no_risk = calculate_no_risk(orders)
upcoming_deliveries = calculate_upcoming_deliveries(orders)
high_priority = calculate_high_priority_orders(orders)


print("Total Orders:", total_orders)
print("No Risk:", no_risk)
print("Upcoming Deliveries:", upcoming_deliveries)

print("Operations:")

for order in orders:
    priority = calculate_priority(order)
    decision = calculate_decision(order)
    days_until_delivery = calculate_days_until_delivery(order)

    print(
        order.order_id,
        "-",
        order.customer,
        "| Priority:",
        priority,
        "| Days Until Delivery:",
        days_until_delivery,
        "| Decision:",
        decision
    )

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
        "| Days Until Delivery:",
        calculate_days_until_delivery(order)
    )

print("NO ACTION REQUIRED")

for order in no_actions:
    print(
        order.order_id,
        "-",
        order.customer
    )