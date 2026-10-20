from decimal import Decimal
from typing import Literal, Optional
from pydantic import BaseModel,ConfigDict,Field

BASIC_SALARY = dict(gt=5_000,lt=1_000_000)
GENDER = Literal["Male", "Female", "Other"]     
DEPARTMENT = Literal["IT","HR","Finance"]

class Base(BaseModel):
    pass

#general salary body 
class EmployeeSalaryResponse(Base):

    model_config = ConfigDict(from_attributes=True)
    
    employee_id: int
    basic_salary: float
    da: float
    pf: float
    gross_salary: float

#create a new employee with personal details 
class CreateEmployeeDetails(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id: int = Field(ge=1)
    employee_name: str = Field(min_length=2, max_length=50,default="")
    gender: GENDER = Field(default="")
    department :DEPARTMENT= Field(default="")



#create a new employee with salary details 
class CreateEmployeeSalary(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id :int = Field(ge=1)
    basic_salary : float = Field(**BASIC_SALARY)

#for the increment 
class IncrementRequest(Base):
    model_config = ConfigDict(extra='forbid')

    percent : float = Field(gt=0,le=100) 

#for the increament response body 
class IncrementResponse(Base):
    message: str
    details: Optional[EmployeeSalaryResponse] = None

#for the department wise total salary
class DepartmentTotalResponse(Base):
    department: str
    Department_total_salary: float