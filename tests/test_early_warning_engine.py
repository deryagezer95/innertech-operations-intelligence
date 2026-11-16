from datetime import date

from order_model import Order
from early_warning_engine import evaluate_early_warning


def create_order(estimated_date, delivery_date, status="In Progress"):
    return Order(
        order_id="TEST-001",
        customer="Test Customer",
        product="Test Product",
        quantity=100,
        delivery_date=delivery_date,
        status=status,
        estimated_completion_date=estimated_date,
    )


def test_detects_delay_risk():
    order = create_order(
        date(2026, 11, 24),
        date(2026, 11, 21)
    )
    assert evaluate_early_warning(order) == "DELAY_RISK"


def test_detects_low_buffer():
    order = create_order(
        date(2026, 11, 21),
        date(2026, 11, 21)
    )
    assert evaluate_early_warning(order) == "LOW_BUFFER"


def test_detects_on_track():
    order = create_order(
        date(2026, 11, 18),
        date(2026, 11, 21)
    )
    assert evaluate_early_warning(order) == "ON_TRACK"


def test_detects_missing_estimated_date():
    order = create_order(None, date(2026, 11, 21))
    assert evaluate_early_warning(order) == "INSUFFICIENT_DATA"


def test_completed_order():
    order = create_order(
        None,
        date(2026, 11, 21),
        status="Completed"
    )
    assert evaluate_early_warning(order) == "COMPLETED"