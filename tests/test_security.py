from inventory_tools import get_inventory_details


def test_cross_site_access_denied():
    result = get_inventory_details("SKU-8805")

    assert result["success"] is False
    assert result["error_code"] == "ACCESS_DENIED"