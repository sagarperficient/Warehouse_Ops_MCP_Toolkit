# Warehouse Ops MCP Toolkit - Agent Demonstration

This transcript demonstrates typical interactions between a warehouse operator and the Warehouse Ops MCP Toolkit.

---

# Scenario 1 - Ambiguous Inventory Search

## User

Do we have pallet wrap?

## Agent

I found multiple matching products:

1. SKU-8801 - Pallet wrap, 500mm clear
2. SKU-8802 - Pallet wrap, 500mm black

Please specify which product you mean.

## Outcome

The toolkit returned multiple candidates and the agent requested clarification rather than guessing.

---

# Scenario 2 - Inventory Lookup

## User

Show me SKU-8801

## Agent

Inventory Details

SKU: SKU-8801

Description: Pallet wrap, 500mm clear

Site: LEEDS-01

Bin Location: A-12-3

Quantity: 240

Unit: each

## Outcome

The user received detailed inventory information for a single SKU.

---

# Scenario 3 - Invalid SKU Lookup

## User

Show me SKU-9999

## Agent

Error: INVALID_SKU

SKU 'SKU-9999' was not found.

Suggestion:

Use inventory search to locate available products.

## Outcome

The toolkit returned an actionable error message instead of a generic system error.

---

# Scenario 4 - Cross-Site Security Enforcement

## User

Show me inventory from Reading warehouse

## Agent

Access denied.

Your assigned warehouse site is LEEDS-01.

Cross-site inventory access is not permitted.

## Outcome

The toolkit enforced site-based security controls and prevented unauthorized access.

---

# Scenario 5 - Stock Adjustment Confirmation

## User

Adjust SKU-8801 quantity to 300

## Agent

Confirmation Required

This action affects inventory records and month-end reconciliation processes.

Do you want to continue?

## User

Yes

## Agent

Stock quantity updated successfully.

SKU: SKU-8801

Previous Quantity: 240

New Quantity: 300

## Outcome

The toolkit enforced a confirmation workflow before performing a state-changing operation.

---

# Demonstrated Capabilities

- Inventory Search
- Inventory Retrieval
- Clarification and Disambiguation
- Site-Based Security
- Actionable Error Handling
- Confirmation Workflow
- Safe State-Changing Operations

The transcript demonstrates that the Warehouse Ops MCP Toolkit supports reliable, secure, and agent-friendly warehouse operations.