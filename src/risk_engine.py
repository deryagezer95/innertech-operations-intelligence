from datetime import date

from order_model import Order


def find_delay_risks(orders: list[Order]) -> list[Order]:
    risks = []

    for order in orders:
        if order.status != "Completed" and order.delivery_date < date.today():
            risks.append(order)

    return risks