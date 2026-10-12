from unittest.mock import create_autospec

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun_mock = create_autospec(Bun, instance=True)
    bun_mock.get_name.return_value = "white bun"
    bun_mock.get_price.return_value = 100
    return bun_mock


@pytest.fixture
def ingredient_factory():
    def make_ingredient(name, price, ingredient_type=INGREDIENT_TYPE_FILLING):
        ingredient_mock = create_autospec(Ingredient, instance=True)
        ingredient_mock.get_name.return_value = name
        ingredient_mock.get_price.return_value = price
        ingredient_mock.get_type.return_value = ingredient_type
        return ingredient_mock

    return make_ingredient
