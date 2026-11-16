import csv
from pathlib import Path
from datetime import date

from order_model import Order


file_path = Path(__file__).resolve().parent.parent / "data" / "orders.csv"


def load_orders() -> list[Order]:
    orders = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            estimated_date_raw = row.get(
                "estimated_completion_date", ""
            ).strip()

            estimated_date = (
                date.fromisoformat(estimated_date_raw)
                if estimated_date_raw
                else None
            )

            order = Order(
                order_id=row["order_id"],
                customer=row["customer"],
                product=row["product"],
                quantity=int(row["quantity"]),
                delivery_date=date.fromisoformat(row["delivery_date"]),
                status=row["status"],
                estimated_completion_date=estimated_date,
            )

            orders.append(order)

    return orders