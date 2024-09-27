from datetime import datetime
from typing import TypeVar, Generic
from uuid import UUID

TKey = TypeVar("TKey", int, UUID) # addded constraint that TKey can be either int or UUID
TValue = TypeVar("TValue")

class Record(Generic[TKey, TValue]):
    created: datetime
    key: TKey
    value: TValue

    def __init__(self, key: TKey, value: TValue):
        self.key = key
        self.value = value
    
    def update(self, value: TValue):
        self.value = value


record1 = Record(1, "Hello") # Record[int, str]
record1.update("new word") # update(value: str)
# record1.update(1)  # typing error as we have set the TValue as a string for this record


record2 = Record(1, 20) # Record[int, int]
record2.update(30) # update(value: int)
# record2.update("new value")  # typing error as we have set the TValue as a int for this record
