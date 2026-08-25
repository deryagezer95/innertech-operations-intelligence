from decision_engine import calculate_decision
from delivery_engine import calculate_days_until_delivery
def get_days_late(order):
    return -calculate_days_until_delivery(order)
def build_action_queue(orders):
    immediate_actions = []
    reviews = []
    monitors = []
    no_actions = []
    for order in orders:
        decision = calculate_decision(order)
        if decision == "Immediate Action":
            immediate_actions.append(order)

        elif decision == "Review":
            reviews.append(order)

        elif decision == "Monitor":
            monitors.append(order)

        else:
            no_actions.append(order)
    immediate_actions = sorted(immediate_actions, key=get_days_late, reverse=True)
    reviews = sorted(reviews, key=get_days_late, reverse=True)
    monitors = sorted(
    monitors,
    key=calculate_days_until_delivery
)
    return immediate_actions, reviews, monitors, no_actions