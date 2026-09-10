# Warehouse Ops MCP Toolkit Specification

## Purpose

Design an MCP toolkit that enables warehouse operators to:

- Search inventory
- View inventory details
- Manage dock operations
- Raise and resolve exceptions
- Maintain inventory integrity

This specification intentionally differs from the original Ops request where a single tool combined multiple responsibilities.

---

# Design Changes

## Change 1: lookup → search_inventory + get_inventory_details

Reason:

The stock data contains multiple similar products such as:

- Pallet wrap, 500mm clear
- Pallet wrap, 500mm black

A single lookup operation could cause the agent to confidently choose the wrong SKU.

---

## Change 2: check_dock split into three tools

Original:

- View dock availability
- Book dock
- Cancel booking

New:

- get_dock_availability
- book_dock_slot
- cancel_dock_booking

Reason:

Read and write operations should be separate.

---

## Change 3: stock_change split into two tools

Original:

- Quantity adjustment
- Bin movement

New:

- adjust_stock_quantity
- move_inventory_bin

Reason:

Inventory adjustments affect stock valuation and month-end counting.
Bin movement changes location only.

---

# Site Security Model

All tools operate within the authenticated user's assigned site.

Users cannot access:

- Other warehouse sites
- Cross-site inventory information
- Cross-site dock operations

Site is derived from session context and never accepted as a tool parameter.

---

# Error Shape

{
  "error_code": "INVALID_SKU",
  "message": "SKU not found",
  "suggestion": "Use search_inventory first"
}

---

# Tool Definitions

## search_inventory

Description:
Search inventory using SKU or partial description.

Input

{
  "query": "pallet wrap"
}

Output

{
  "matches": []
}

---

## get_inventory_details

Description:
Get detailed information for a single SKU.

Input

{
  "sku": "SKU-8801"
}

---

## get_dock_availability

Description:
View available dock slots.

---

## book_dock_slot

Description:
Reserve an available dock slot.

---

## cancel_dock_booking

Description:
Cancel an existing booking.

---

## adjust_stock_quantity

Description:
Correct inventory counts.

Requires confirmation.

---

## move_inventory_bin

Description:
Move inventory between bins.

---

## create_exception

Description:
Raise damage or missing inventory exception.

---

## resolve_exception

Description:
Resolve an existing exception.