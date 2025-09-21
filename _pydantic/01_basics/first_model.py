from pydantic import  BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_dat = {'id': 101, 'name': 'vivke', 'is_active':True} # try passing 23 to is_active

user = User(**input_dat)

print(user)


## all pydnatic models innherit baseModel, import BaseModel
## type annotations
## unpack dict, don't pass it directly ** - Model initiation
## pydantic implictely tries to convert the datatype if possible, else raises validationError

input_dat = {'id': '101', 'name': 'vivke', 'is_active':True}  ## here pydantic converts '101' (str) to 101 (int), if possible
user1=User(**input_dat)

print(user1)

# model ensures the data integrity at the point of its creation