from datetime import date

def calculate_days_until_delivery(order):
    return (order.delivery_date - date.today()).days