from datetime import date

from risk_engine import find_delay_risks

from delivery_engine import calculate_days_until_delivery

from priority_engine import calculate_priority


def calculate_total_orders(orders):
    return len(orders)


def calculate_no_risk(orders):
    risks = find_delay_risks(orders)
    return len(orders) - len(risks)


def calculate_upcoming_deliveries(orders):
    count = 0
    for order in orders:
        days_until_delivery = calculate_days_until_delivery(order)
        if 0 <= days_until_delivery <= 3:
            count += 1
    return count
def calculate_high_priority_orders(orders):
    count = 0
    for order in orders:
        priority = calculate_priority(order)
        if priority.startswith("HIGH"):
            count += 1
    return count