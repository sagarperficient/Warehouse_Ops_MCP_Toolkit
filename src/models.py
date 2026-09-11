from pydantic import BaseModel
from enum import Enum


class Site(str, Enum):
    LEEDS = "LEEDS-01"
    READING = "READING-02"
    GLASGOW = "GLASGOW-03"


class InventoryItem(BaseModel):
    sku: str
    description: str
    site: str
    bin: str
    quantity: int
    unit: str


class ExceptionCategory(str, Enum):
    DAMAGED = "DAMAGED"
    MISSING = "MISSING"
    QUALITY = "QUALITY"