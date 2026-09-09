from datetime import date, timedelta
from order_model import Order
from action_queue import build_action_queue
def  test_most_delayed_order_comes_first():
    order1 = Order(
        order_id="TEST-001",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=10),
        status="In Progress"
    )
    order2 = Order(
        order_id="TEST-002",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=3),
        status="In Progress"
    )
    action_queue = build_action_queue([order1, order2])
    assert action_queue[0][0].order_id == "TEST-001"
def test_most_delayed_review_order_comes_first():
    order1 = Order(
        order_id="TEST-003",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=6),
        status="In Progress"
    )
    order2 = Order(
        order_id="TEST-004",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=3),
        status="In Progress"
    )
    action_queue = build_action_queue([order1, order2])
    assert action_queue[1][0].order_id == "TEST-003"
def test_nearest_monitor_order_comes_first():
    order1 = Order(
        order_id="TEST-005",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() + timedelta(days=2),
        status="In Progress"
    )
    order2 = Order(
        order_id="TEST-006",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() + timedelta(days=10),
        status="In Progress"
    )
    action_queue = build_action_queue([order1, order2])
    assert action_queue[2][0].order_id == "TEST-005"
def test_completed_order_goes_to_no_action_required():
    order1 = Order(
        order_id="TEST-007",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today(),
        status="Completed"
    )
    order2 = Order(
        order_id="TEST-008",
        customer="Test Customer",
        product="Test Product",
        quantity=10,
        delivery_date=date.today() - timedelta(days=3),
        status="in progress"
    )
    action_queue = build_action_queue([order1, order2])
    assert action_queue[3][0].order_id == "TEST-007"