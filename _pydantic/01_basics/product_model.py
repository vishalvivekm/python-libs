from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # default


product_one = Product(id=1, name='Laptop', price=399.99, in_stock=True)

product_two = Product(id=2, name="mouse", price=23.44)

# product_three= Product(name="keyboard") ## validation error

## alwyas user type annotation
## int, float, str, bool etc
## set sensible default

# pydantic automatically tries to convert data types for us, if it can
## "1231" -> 123
# "true" -> True
## 123 -> 123.0

## pydantic and typing --> data types

