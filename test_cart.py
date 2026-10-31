from cart import line_total


def test_small_order_pays_full_price():
    assert line_total(2.50, 4) == 10.00


def test_bulk_discount_starts_at_ten():
    assert line_total(2.50, 10) == 22.50
