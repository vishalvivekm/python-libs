from pydantic import BaseModel

from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str] # typing -> List, pydantic -> int, result: List[str]
    quantities: Dict[str, str]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # optional, but a str if present, by default None

## List[str]

## Dict[str, int]

## Optional = optional but a string or None

cart_data = {
    "user_id": 123,
    "items": ["laptop", "mouse", "keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

# cart = Cart(cart_data)
cart = Cart(**cart_data) 

