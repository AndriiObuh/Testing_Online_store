from store.order_service import create_order


def test_create_order_success():
    items = [
        {"name": "Laptop", "price": 1000.0, "quantity": 1},
        {"name": "Mouse", "price": 50.0, "quantity": 2}
    ]
    order = create_order("Andrii", items)
    assert order["customer"] == "Andrii"
    assert order["status"] == "created"
    assert order["total"] == 1100
    assert len(order['items']) == 2
