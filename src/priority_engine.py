from datetime import date
from delivery_engine import calculate_days_until_delivery
def calculate_delay(order):
    if order.delivery_date < date.today():
        days_late = (date.today() - order.delivery_date).days
        return days_late
    return 0

def calculate_priority(order):
    if order.status == "Completed":
     return "LOW"

    if order.delivery_date < date.today():

        days_late = calculate_delay(order)

        if days_late >= 7:
            return "HIGH — 7+ days late"

        if days_late < 7:
            return "MEDIUM — 1–6 days late"

    days_until_delivery = calculate_days_until_delivery(order)
    return f"LOW — {days_until_delivery} days until delivery"