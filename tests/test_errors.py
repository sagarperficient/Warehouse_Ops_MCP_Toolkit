from src.inventory_tools import get_inventory_details


def test_invalid_sku():
    result = get_inventory_details("INVALID")

    assert result["success"] is False
    assert result["error_code"] == "INVALID_SKU"