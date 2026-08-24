from datetime import date
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
            return "HIGH"

        if days_late < 7:
            return "MEDIUM"

    days_until_delivery = (order.delivery_date - date.today()).days
    return "LOW"