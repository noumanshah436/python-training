from datetime import datetime
from typing import Generic, TypeVar
from pydantic import BaseModel

# old syntax:

# T = TypeVar("T")

# class UserInputField(BaseModel, Generic[T]):
#     user_input: T | None = None
#     user_input_time: datetime | None = None

# deal_value: UserInputField[int] = UserInputField(user_input=12)


# *************************

# New syntax:


class UserInputField[T](BaseModel):
    user_input: T | None = None
    user_input_time: datetime | None = None


deal_value_int: UserInputField[int] = UserInputField[int](user_input=12)
print(f"deal_value_int ------------------------{deal_value_int}")


deal_value_float: UserInputField[float] = UserInputField[float](user_input=12.23)
print(f"deal_value_float ------------------------{deal_value_float}")


# To check typing run:
# mypy --enable-incomplete-feature=NewGenericSyntax "python_built_in_modules/type_annotations/generics/6_generic_models.py"
