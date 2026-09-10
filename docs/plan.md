# Implementation Plan

## Architecture

Agent Host
    |
    |
Warehouse MCP Server
    |
    +-- Inventory Service
    +-- Dock Service
    +-- Exception Service

## Components

### Inventory Service

- search_inventory
- get_inventory_details
- adjust_stock_quantity
- move_inventory_bin

### Dock Service

- get_dock_availability
- book_dock_slot
- cancel_dock_booking

### Exception Service

- create_exception
- resolve_exception

## Security

Site isolation enforced inside toolkit.

## Testing

- Tool invocation
- Schema validation
- Site scope validation
- Confirmation workflow
- Error handling

## Agent Host

VS Code MCP Host
or
Claude Desktop MCP