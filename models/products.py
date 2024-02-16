from pydantic import BaseModel, ConfigDict
from typing import Optional


class Product(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: Optional[str] = None
    name: str
    description: str
    price: int
    status: bool = True

class ProductIn(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    name: str
    description: str
    price: int
    status: bool = True