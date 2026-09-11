# Reflection

## Overview

The objective of this case study was to design a Warehouse Operations MCP Toolkit that warehouse operators can use efficiently through an AI agent. Rather than implementing the original Operations wish-list directly, the solution focused on creating agent-friendly interfaces, enforcing security controls, supporting clarification workflows, and improving operational reliability.

---

## Changes from the Original Design

### 1. Lookup Tool Redesign

#### Original Request

lookup

#### Implemented Design

- search_inventory
- get_inventory_details

#### Reason

The inventory dataset contains multiple products with very similar descriptions, for example:

- Pallet wrap, 500mm clear
- Pallet wrap, 500mm black

A single lookup tool returning a single result could cause the agent to confidently select the wrong SKU.

The redesigned approach separates searching and item retrieval. The search tool returns all matching candidates and indicates when clarification is required. This allows the agent to ask follow-up questions rather than making assumptions.

---

### 2. Dock Tool Redesign

#### Original Request

check_dock

#### Implemented Design

- get_dock_availability
- book_dock_slot
- cancel_dock_booking

#### Reason

The original request combined both read and write operations into a single tool.

Separating these operations improves clarity for both agents and users. Read-only actions and state-changing actions are clearly distinguished, reducing the risk of unintended updates.

---

### 3. Stock Change Tool Redesign

#### Original Request

stock_change

#### Implemented Design

- adjust_stock_quantity
- move_inventory_bin

#### Reason

These operations represent different business actions.

Inventory quantity adjustments impact stock records and inventory reconciliation processes, while inventory movement only changes the physical storage location.

Separating these actions makes the workflow easier to understand and supports additional controls such as confirmation requirements.

---

## Security Design

Warehouse operators should only access information belonging to their assigned warehouse site.

The toolkit enforces site-based access control internally and does not rely on user-supplied site parameters.

Example:

- LEEDS-01 operators can access LEEDS-01 inventory.
- LEEDS-01 operators cannot access READING-02 inventory.
- LEEDS-01 operators cannot access GLASGOW-03 inventory.

This prevents unauthorized cross-site visibility and aligns with the requirements specified by Operations.

---

## Error Handling Design

The Operations team highlighted issues with generic error codes.

Instead of returning messages such as:

ERR_4001

the toolkit returns actionable error responses containing:

- Error code
- Human-readable message
- Suggested corrective action

Example:

```json
{
  "error_code": "INVALID_SKU",
  "message": "SKU not found",
  "suggestion": "Use search_inventory first"
}