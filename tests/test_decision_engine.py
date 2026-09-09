from datetime import date, timedelta
from order_model import Order
from decision_engine import calculate_decision


def test_high_priority_is_immediate_action():
    order = Order(
        order_id="TEST-001",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=7),
        status="In Progress"
    )
    assert calculate_decision(order) == "Immediate Action"
def test_medium_priority_is_review():
    order = Order(
        order_id="TEST-002",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=3),
        status="In Progress"
    )
    assert calculate_decision(order) == "Review"
def test_completed_order_is_no_action_required():
    order = Order(
        order_id="TEST-003",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today(),
        status="Completed"
    )
    assert calculate_decision(order) == "No Action Required"
def test_medium_priority_is_review_for_six_days_late():
    order = Order(
        order_id="TEST-004",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=6),
        status="In Progress"
    )
    assert calculate_decision(order) == "Review"
def test_low_priority_is_monitor():
    order = Order(
        order_id="TEST-005",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() + timedelta(days=5),
        status="In Progress"
    )
    assert calculate_decision(order) == "Monitor"    