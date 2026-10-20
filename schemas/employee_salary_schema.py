from decimal import Decimal
from typing import Literal
from pydantic import BaseModel,ConfigDict,Field

BASIC_SALARY = dict(gt=5_000,lt=1_000_000)
Gender = Literal["Male", "Female", "Other"]     

class Base(BaseModel):
    pass


class EmployeeSalaryResponse(Base):

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    basic_salary: float
    da: float
    pf: float
    gross_salary: float


class CreateEmployeeSalary(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id :int = Field(ge=1)
    basic_salary : float = Field(**BASIC_SALARY)


# class UpdateEmployee(Base):
#     model_config = ConfigDict(extra='forbid')

#     basic_salary : float = Field(**BASIC_SALARY)

class IncrementRequest(Base):
    model_config = ConfigDict(extra='forbid')

    percent : float = Field(gt=0,le=100) 

class CreateEmployeeDetails(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id: int = Field(ge=1)
    employee_name: str = Field(min_length=2, max_length=50)
    gender: Gender


class IncrementResponse(Base):
    message: str
    details: EmployeeSalaryResponse