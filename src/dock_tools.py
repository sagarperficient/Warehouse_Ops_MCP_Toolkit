# src/dock_tools.py

def get_dock_availability():
    return {
        "available_slots": [
            "DOCK-A-10:00",
            "DOCK-B-14:00"
        ]
    }


def book_dock_slot(slot_id: str):
    return {
        "success": True,
        "message": f"Dock slot {slot_id} booked"
    }


def cancel_dock_booking(slot_id: str):
    return {
        "success": True,
        "message": f"Dock slot {slot_id} cancelled"
    }