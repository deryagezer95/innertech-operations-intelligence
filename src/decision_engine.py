from priority_engine import calculate_priority
def calculate_decision(order):
    if order.status == "Completed":
        return "No Action Required"
    priority = calculate_priority(order)
    if priority.startswith("HIGH"):
        return "Immediate Action"
    elif priority.startswith("MEDIUM"):
        return "Review"
    else:
        return "Monitor"
