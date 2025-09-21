from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # required field
        min_length = 3, # 3 chars long at leat
        max_length=50,
        description="Employee name",
        examples="Vivek Vishal"
    )
    department: Optional[str] = 'General' # optional string field, defaulting to 'General'
    salary: float = Field(
        ...,
        ge=100000,
        le = 1000000,
        description="Annual Salary in USD"
    )

## Field: min_length, max_length, ge, gt, le, lt, regex

# field parameters


