# src/exception_tools.py

def create_exception(category: str, sku: str, description: str):
    return {
        "ticket_id": "EXC-001",
        "category": category,
        "sku": sku,
        "status": "OPEN"
    }


def resolve_exception(ticket_id: str, resolution_note: str):
    return {
        "ticket_id": ticket_id,
        "status": "RESOLVED",
        "resolution": resolution_note
    }