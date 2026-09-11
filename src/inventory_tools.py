from pathlib import Path

import pandas as pd

from src.security import (
    get_current_site,
    has_site_access,
    access_denied_response
)

# Load inventory data
DATA_FILE = Path(__file__).parent.parent / "data" / "stock_snapshot.csv"

df = pd.read_csv(DATA_FILE)


def search_inventory(query: str):
    """
    Search inventory by SKU or description.

    Results are automatically restricted
    to the user's assigned warehouse site.
    """

    current_site = get_current_site()

    matches = df[
        (
            df["description"].str.contains(
                query,
                case=False,
                na=False
            )
            |
            df["sku"].str.contains(
                query,
                case=False,
                na=False
            )
        )
        &
        (df["site"] == current_site)
    ]

    results = matches.to_dict(orient="records")

    return {
        "success": True,
        "query": query,
        "site": current_site,
        "match_count": len(results),
        "requires_disambiguation": len(results) > 1,
        "matches": results
    }


def get_inventory_details(sku: str):
    """
    Retrieve inventory details for an SKU.

    Access is restricted to the user's site.
    """

    current_site = get_current_site()

    result = df[
        (df["sku"] == sku)
        &
        (df["site"] == current_site)
    ]

    if result.empty:

        sku_exists = df[df["sku"] == sku]

        if not sku_exists.empty:
            site = sku_exists.iloc[0]["site"]

            if not has_site_access(site):
                return access_denied_response(site)

        return {
            "success": False,
            "error_code": "INVALID_SKU",
            "message": f"SKU '{sku}' not found.",
            "suggestion": (
                "Use search_inventory() "
                "to locate available items."
            )
        }

    return {
        "success": True,
        "site": current_site,
        "data": result.iloc[0].to_dict()
    }


def adjust_stock_quantity(
    sku: str,
    new_quantity: int,
    confirmation: bool = False,
):
    """
    Adjust stock quantity.

    Requires explicit confirmation because
    inventory corrections affect stock records.
    """

    if not confirmation:
        return {
            "success": False,
            "confirmation_required": True,
            "reason": (
                "Inventory corrections affect "
                "stock records and month-end counts."
            ),
            "message": (
                "Re-submit with confirmation=True "
                "to continue."
            )
        }

    current_site = get_current_site()

    item = df[
        (df["sku"] == sku)
        &
        (df["site"] == current_site)
    ]

    if item.empty:

        sku_exists = df[df["sku"] == sku]

        if not sku_exists.empty:
            site = sku_exists.iloc[0]["site"]

            if not has_site_access(site):
                return access_denied_response(site)

        return {
            "success": False,
            "error_code": "INVALID_SKU",
            "message": f"SKU '{sku}' not found."
        }

    old_quantity = int(item.iloc[0]["quantity"])

    return {
        "success": True,
        "sku": sku,
        "site": current_site,
        "old_quantity": old_quantity,
        "new_quantity": new_quantity,
        "message": "Stock quantity updated."
    }


def move_inventory_bin(
    sku: str,
    target_bin: str,
):
    """
    Record movement of inventory
    from one bin location to another.
    """

    current_site = get_current_site()

    item = df[
        (df["sku"] == sku)
        &
        (df["site"] == current_site)
    ]

    if item.empty:

        sku_exists = df[df["sku"] == sku]

        if not sku_exists.empty:
            site = sku_exists.iloc[0]["site"]

            if not has_site_access(site):
                return access_denied_response(site)

        return {
            "success": False,
            "error_code": "INVALID_SKU",
            "message": f"SKU '{sku}' not found."
        }

    current_bin = item.iloc[0]["bin"]

    return {
        "success": True,
        "sku": sku,
        "site": current_site,
        "source_bin": current_bin,
        "target_bin": target_bin,
        "message": "Inventory transfer recorded."
    }