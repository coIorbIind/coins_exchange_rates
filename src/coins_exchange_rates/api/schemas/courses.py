from decimal import Decimal

from pydantic import BaseModel


class CourseSchema(BaseModel):
    direction: str
    value: Decimal


class ExchangerSchema(BaseModel):
    exchanger: str
    courses: list[CourseSchema]
