from datetime import datetime

from pydantic import BaseModel


class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    dob: datetime
