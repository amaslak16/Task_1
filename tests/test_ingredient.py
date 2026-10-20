import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    "ingredient_type",
    [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
    ids=["sauce", "filling"],
)
def test_get_type_returns_ingredient_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "cutlet", 100.0)

    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize(
    "name",
    ["hot sauce", "cutlet"],
    ids=["sauce-name", "filling-name"],
)
def test_get_name_returns_ingredient_name(name):
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100.0)

    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    "price",
    [100.0, 0.0],
    ids=["regular-price", "zero-price"],
)
def test_get_price_returns_ingredient_price(price):
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", price)

    assert ingredient.get_price() == price
