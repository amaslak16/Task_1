import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name",
    ["white bun", "black bun"],
    ids=["white-bun", "black-bun"],
)
def test_get_name_returns_bun_name(name):
    bun = Bun(name, 200.0)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    "price",
    [200.0, 0.0],
    ids=["regular-price", "zero-price"],
)
def test_get_price_returns_bun_price(price):
    bun = Bun("white bun", price)

    assert bun.get_price() == price
