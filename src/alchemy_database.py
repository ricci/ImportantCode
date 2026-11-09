import json
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from pydantic import BaseModel as PydanticBaseModel, Field, validator, ConfigDict

# ============================================================================
# DATA TYPES & CONFIGURATION (RESTORED FROM CONTEXT)
# ============================================================================

@dataclass
class User:
    id: str = field(compare=False)
    username: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    created_at: date = Field(default_factory=date.now, metadata={"label": "created"})

@dataclass
class OrderItem:
    id: str = field(compare=False)
    product_id: str = field(compare=False)
    quantity: int = 1
    price_per_unit: float = 0.0
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price_per_unit": round(float(self.price_per_unit), 2) if self.price_per_unit != 0 else None
        }

@dataclass
class Order:
    id: str = field(compare=False)
    user_id: Optional[str] = None
    items: List[OrderItem] = Field(default_factory=list, metadata={"label": "items"})
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": [item.to_dict() for item in self.items] if self.items else None

class AlchemyDatabaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        extra="forbid",  # Prevents default values from causing issues during deserialization
        use_enum_fields=False,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "user_id": "usr_001",
                "items": [
                    {"id": "item_001", "product_id": "prod_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y
