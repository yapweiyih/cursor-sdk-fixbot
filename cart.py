"""Shopping cart pricing."""

BULK_THRESHOLD = 10
BULK_DISCOUNT = 0.10


def line_total(price: float, qty: int) -> float:
    """Price for one cart line. Ten or more units get the bulk discount."""
    total = price * qty
    if qty >= BULK_THRESHOLD:
        total *= 1 - BULK_DISCOUNT
    return round(total, 2)
