import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_new_burger_has_no_bun_or_ingredients(burger):
    assert (burger.bun, burger.ingredients) == (None, [])


def test_set_buns_keeps_the_selected_bun(burger, bun):
    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_keeps_each_instance_in_order(burger, ingredient_factory):
    first = ingredient_factory("cutlet", 100)
    second = ingredient_factory("cutlet", 100)

    burger.add_ingredient(first)
    burger.add_ingredient(second)

    assert burger.ingredients == [first, second]


def test_remove_ingredient_deletes_only_selected_position(burger, ingredient_factory):
    first = ingredient_factory("cutlet", 100)
    second = ingredient_factory("cheese", 50)
    burger.ingredients = [first, second, first]

    burger.remove_ingredient(1)

    assert burger.ingredients == [first, first]


def test_remove_ingredient_rejects_out_of_range_index(burger, ingredient_factory):
    ingredient = ingredient_factory("cutlet", 100)
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.remove_ingredient(1)

    assert burger.ingredients == [ingredient]


@pytest.mark.parametrize(
    "old_index, new_index, expected_order",
    [(0, 2, (1, 2, 0)), (2, 0, (2, 0, 1))],
    ids=["first-to-last", "last-to-first"],
)
def test_move_ingredient_changes_position_without_losing_items(
    burger, ingredient_factory, old_index, new_index, expected_order
):
    first = ingredient_factory("cutlet", 100)
    second = ingredient_factory("cheese", 50)
    third = ingredient_factory("salad", 20)
    ingredients = [first, second, third]
    burger.ingredients = ingredients.copy()

    burger.move_ingredient(old_index, new_index)

    assert burger.ingredients == [ingredients[index] for index in expected_order]


def test_move_ingredient_rejects_out_of_range_source_index(burger, ingredient_factory):
    ingredient = ingredient_factory("cutlet", 100)
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.move_ingredient(1, 0)

    assert burger.ingredients == [ingredient]


@pytest.mark.parametrize(
    "bun_price, ingredient_data, expected_price",
    [
        (100, [], 200),
        (40, [("cutlet", 50)], 130),
        (100, [("cutlet", 50), ("cutlet", 50), ("salad", 20)], 320),
    ],
    ids=["no-ingredients", "different-bun-price", "two-cutlets-and-salad"],
)
def test_get_price_counts_two_buns_and_every_ingredient(
    burger, bun, ingredient_factory, bun_price, ingredient_data, expected_price
):
    """В цену входят две булочки и каждый ингредиент, включая повторяющиеся."""
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)
    for name, price in ingredient_data:
        burger.add_ingredient(ingredient_factory(name, price))

    assert burger.get_price() == expected_price


@pytest.mark.parametrize(
    "bun_name, bun_price, ingredients, expected_receipt",
    [
        ("white bun", 100, [], "(==== white bun ====)\n(==== white bun ====)\n\nPrice: 200"),
        (
            "black bun",
            40,
            [("hot sauce", 20, INGREDIENT_TYPE_SAUCE), ("cutlet", 50, INGREDIENT_TYPE_FILLING)],
            "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n"
            "(==== black bun ====)\n\nPrice: 150",
        ),
    ],
    ids=["empty", "sauce-and-filling"],
)
def test_get_receipt_lists_bun_ingredients_and_total(
    burger, bun, ingredient_factory, bun_name, bun_price, ingredients, expected_receipt
):
    bun.get_name.return_value = bun_name
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)
    for name, price, ingredient_type in ingredients:
        burger.add_ingredient(ingredient_factory(name, price, ingredient_type))

    assert burger.get_receipt() == expected_receipt
