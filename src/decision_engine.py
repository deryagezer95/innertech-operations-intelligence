from priority_engine import calculate_priority
from early_warning_engine import evaluate_early_warning


def calculate_decision(order):

    if order.status.strip().lower() == "completed":
        return "No Action Required"

    # First, check actual delivery delays
    priority = calculate_priority(order)

    if priority.startswith("HIGH"):
        return "Immediate Action"

    elif priority.startswith("MEDIUM"):
        return "Review"

    # Then, check predicted delivery risks
    warning = evaluate_early_warning(order)

    if warning == "DELAY_RISK":
        return "Immediate Action"

    elif warning == "LOW_BUFFER":
        return "Review"

    return "Monitor"