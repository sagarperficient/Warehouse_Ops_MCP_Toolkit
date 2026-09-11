from src.inventory_tools import adjust_stock_quantity


def test_confirmation_required():

    result = adjust_stock_quantity(
        "SKU-8801",
        300
    )

    assert result["success"] is False
    assert result["confirmation_required"] is True


def test_confirmation_accepted():

    result = adjust_stock_quantity(
        "SKU-8801",
        300,
        True
    )

    assert result["success"] is True