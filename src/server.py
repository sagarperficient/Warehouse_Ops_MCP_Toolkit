from inventory_tools import search_inventory
from dock_tools import get_dock_availability
from exception_tools import create_exception

print(search_inventory("pallet wrap"))
print(get_dock_availability())
print(create_exception(
    "DAMAGED",
    "SKU-8801",
    "Packaging damaged"
))