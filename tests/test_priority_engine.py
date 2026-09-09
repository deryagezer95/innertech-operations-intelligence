from datetime import date , timedelta
from order_model import Order
from priority_engine import calculate_priority
def test_completed_order_is_low():
    order = Order(
    order_id="TEST-001",
    customer="Test Customer",
    product="Test Product",
    quantity=10,
    delivery_date=date.today(),
    status="Completed"
)
    assert calculate_priority(order) == "LOW"
    def test_seven_days_late_is_high():
        order = Order(
    order_id="TEST-002",
    customer="Test Customer",
    product="Test Product",
    quantity=10,
    delivery_date=date.today() - timedelta(days=7),
    status="In Progress"
)
        assert calculate_priority(order).startswith("HIGH")
        def test_three_days_late_is_medium():
            order = Order(
    order_id="TEST-003",
    customer="Test Customer",
    product="Test Product",
    quantity=10,
    delivery_date=date.today() - timedelta(days=3),
    status="In Progress"
)
            assert calculate_priority(order).startswith("MEDIUM")
            def test_six_days_late_is_medium():

                order = Order(
    order_id="TEST-004",
    customer="Test Customer",
    product="Test Product",
    quantity=10,
    delivery_date=date.today() - timedelta(days=6),
    status="In Progress"
)
                assert calculate_priority(order).startswith("MEDIUM")