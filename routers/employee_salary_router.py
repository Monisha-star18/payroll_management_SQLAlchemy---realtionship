from fastapi import APIRouter , Depends,Path
from sqlalchemy.ext.asyncio import AsyncSession

from services.employee_salary_service import employee_salary_service
from database import get_session

from schemas import (IncrementResponse, 
                     IncrementRequest, 
                     CreateEmployeeDetails,
                     CreateEmployeeSalary,
                     DepartmentTotalResponse)

router = APIRouter(prefix="/api/employee_salary")

#post the new employee personal details 
#dependency injection
@router.post("/add_employee_deatils")
async def add_employee_deatils(employee_details :CreateEmployeeDetails,db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.add_employee_personalDetails(employee_details,db)


#post the new employee salary details 
@router.post('/add_employee_salary_deatils')
async def create_employee_salary(employee_salary_deatils :CreateEmployeeSalary,
                                 db:AsyncSession = Depends(get_session)
                                ):
    return await employee_salary_service.create_employee(employee_salary_deatils,db)

#get the employee deatils 
@router.get('/{employee_id}')
async def get_all_employee_details(employee_id: int= Path(gt=0),db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.get_all_employee(employee_id,db)


#increment by percentage
@router.post('/{employee_id}/increment',response_model=IncrementResponse)
async def increase_employee_salary(employee_id: int, 
                                   increment_details: IncrementRequest,
                                    db: AsyncSession = Depends(get_session)
                                    ):
    return await employee_salary_service.increase_salary(employee_id, increment_details, db)

#get department wise total salary
@router.get('/',response_model=list[DepartmentTotalResponse])
async def department_totals(db: AsyncSession = Depends(get_session)):
    return await employee_salary_service.get_department_totals(db)
