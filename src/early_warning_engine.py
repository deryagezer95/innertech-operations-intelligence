from order_model import Order


def evaluate_early_warning(order: Order) -> str:

    if order.status.strip().lower() == "completed":
        return "COMPLETED"

    estimated_date = order.estimated_completion_date

    if estimated_date is None:
        return "INSUFFICIENT_DATA"

    if estimated_date > order.delivery_date:
        return "DELAY_RISK"

    if estimated_date == order.delivery_date:
        return "LOW_BUFFER"

    return "ON_TRACK"