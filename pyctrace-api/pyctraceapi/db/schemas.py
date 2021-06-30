from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    dob: datetime
    infected: bool = False


class Location(BaseModel):
    pass


class Relationship(BaseModel):
    pass


class TimedRelationship(Relationship):
    start_dt: datetime
    end_dt: datetime


class VisitRelationship(TimedRelationship):
    type: Literal = "VISIT"


class HouseholdRelationship(TimedRelationship):
    type: Literal = "HOUSEHOLD"


class TransmissionRelationship(TimedRelationship):
    type: Literal = "TRANSMISSION"
