from fastmcp import FastMCP

from inventory_tools import (
    search_inventory,
    get_inventory_details,
    adjust_stock_quantity,
    move_inventory_bin,
)

from dock_tools import (
    get_dock_availability,
    book_dock_slot,
    cancel_dock_booking,
)

from exception_tools import (
    create_exception,
    resolve_exception,
)

# Create MCP Server
mcp = FastMCP("Warehouse Ops MCP Toolkit")


@mcp.tool()
def inventory_search(query: str):
    """Search inventory by SKU or description."""
    return search_inventory(query)


@mcp.tool()
def inventory_details(sku: str):
    """Get inventory details for a SKU."""
    return get_inventory_details(sku)


@mcp.tool()
def adjust_inventory(
    sku: str,
    quantity: int,
    confirmation: bool = False,
):
    """Adjust inventory quantity."""
    return adjust_stock_quantity(
        sku,
        quantity,
        confirmation,
    )


@mcp.tool()
def move_inventory(
    sku: str,
    target_bin: str,
):
    """Move inventory between bins."""
    return move_inventory_bin(
        sku,
        target_bin,
    )


@mcp.tool()
def dock_availability():
    """Get available dock slots."""
    return get_dock_availability()


@mcp.tool()
def dock_booking(slot_id: str):
    """Book a dock slot."""
    return book_dock_slot(slot_id)


@mcp.tool()
def dock_cancel(slot_id: str):
    """Cancel a dock booking."""
    return cancel_dock_booking(slot_id)


@mcp.tool()
def raise_exception(
    category: str,
    sku: str,
    description: str,
):
    """Create an exception ticket."""
    return create_exception(
        category,
        sku,
        description,
    )


@mcp.tool()
def close_exception(
    ticket_id: str,
    resolution_note: str,
):
    """Resolve an exception ticket."""
    return resolve_exception(
        ticket_id,
        resolution_note,
    )


if __name__ == "__main__":
    print("Starting Warehouse Ops MCP Toolkit...")
    mcp.run()
