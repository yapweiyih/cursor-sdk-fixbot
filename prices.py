"""Unit prices from prices.csv."""

import csv
from decimal import Decimal
from pathlib import Path

PRICES = Path(__file__).with_name("prices.csv")


def load_prices(path: Path = PRICES) -> dict[str, Decimal]:
    """SKU to unit price, read from the price list."""
    with path.open(newline="") as f:
        return {row["sku"]: Decimal(row["unit_price"]) for row in csv.DictReader(f)}


def unit_price(sku: str) -> Decimal:
    """Unit price for one SKU; raises KeyError for an unknown SKU."""
    return load_prices()[sku]
