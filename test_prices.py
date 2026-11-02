from decimal import Decimal

import pytest

from prices import load_prices, unit_price


def test_every_sku_has_a_positive_price():
    prices = load_prices()
    assert len(prices) == 470
    assert all(price > Decimal("0") for price in prices.values())


def test_unknown_sku_raises():
    with pytest.raises(KeyError):
        unit_price("NOPE-000")
