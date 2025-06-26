VALID_STATUSES = {"created", "paid", "shipped", "delivered", "cancelled"}


def create_order(customer_name: str, items: list[dict]):
    if not isinstance(customer_name, str) or not customer_name:
        raise ValueError("Невалідне ім'я клієнта")
    if not items or not isinstance(items, list):
        raise ValueError("Список товарів обов’язковий")

    total = 0
    for item in items:
        if not all(k in item for k in ("name", "price", "quantity")):
            raise ValueError("Товар має бути зі всіма полями")
        if not isinstance(item["price"], (int, float)) or item["price"] <= 0:
            raise ValueError("Ціна має бути додатнім числом")
        if not isinstance(item["quantity"], int) or item["quantity"] <= 0:
            raise ValueError("Кількість має бути додатнім цілим")
        total += item["price"] * item["quantity"]

    return {
        "customer": customer_name,
        "status": "created",
        "total": round(total, 2),
        "items": items
    }


def update_order_status(order: dict, new_status: str):
    if new_status not in VALID_STATUSES:
        raise ValueError("Невалідний статус")
    order["status"] = new_status
    return order
