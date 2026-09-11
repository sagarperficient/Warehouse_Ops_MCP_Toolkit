from src.inventory_tools import search_inventory


def test_search_inventory():
    result = search_inventory("pallet wrap")

    assert result["requires_disambiguation"] is True
    assert result["match_count"] == 2