from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_database_provides_available_buns():
    buns = Database().available_buns()

    assert [(type(bun), bun.get_name(), bun.get_price()) for bun in buns] == [
        (Bun, "black bun", 100),
        (Bun, "white bun", 200),
        (Bun, "red bun", 300),
    ]


def test_database_provides_available_ingredients():
    ingredients = Database().available_ingredients()

    assert [
        (type(ingredient), ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
        for ingredient in ingredients
    ] == [
        (Ingredient, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (Ingredient, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (Ingredient, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (Ingredient, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (Ingredient, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (Ingredient, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
