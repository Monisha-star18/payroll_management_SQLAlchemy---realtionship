from sqlalchemy.ext.asyncio import AsyncSession

from repositories.employee_salary_repo import EmployeeSalaryRepo
from services.payroll_services import PayrollService
from models import EmployeePayDeatils

class EmployeeSalaryService:

    def __init__(self):
        self.payroll_services=PayrollService()
        self.employee_repository=EmployeeSalaryRepo()
      
    #the payroll calculations 
    def payroll_calutaions(self,basic_salary):
            
            da = self.payroll_services.calculate_da(basic_salary)
            pf=self.payroll_services.calculate_pf(basic_salary)
            gross_salary=self.payroll_services.calculate_gross_salary(basic_salary)
            
            salary_deatils = {"da":da , 
                                "pf":pf,
                                "gross_salary":gross_salary}
    
            return salary_deatils

    

    # #update the employees
    # async def edit_employee(self,employee_deatils,employee_id,db):

    #     basic_salary = employee_deatils.basic_salary

    #     salary_deatils = self.payroll_calutaions(basic_salary)

    #     employee_data = {"employee_id":employee_id , "basic_salary":basic_salary}

    #     employee_compailed_deatils={**employee_data,**salary_deatils}

    #     return await self.employee_repository.put_employee(employee_compailed_deatils,db)

    # #delete employee
    # async def remove_employee(self,employee_id,db):
    #      return await self.employee_repository.delete_employee(employee_id,db)
         
    # #increament
    # async def increase_salary(self, employee_id: int, increment_details, db: AsyncSession) -> EmployeePayDeatils:
        
    #     return await self.employee_repository.increase_salary(employee_id, increment_details.percent, db)

    async def add_employee_personalDetails(self,employee_details,db:AsyncSession):
        return await self.employee_repository.post_employee_personalDetails(employee_details,db)


    #post new employees
    async def create_employee(self,employee_salary_deatils,db:AsyncSession):
        #change the object to dict
        employee_deatils = employee_salary_deatils.model_dump()

        basic_salary = employee_deatils["basic_salary"]

        salary_deatils = self.payroll_calutaions(basic_salary)

        employee_compailed_deatils = {**employee_deatils,**salary_deatils}

        return await self.employee_repository.post_employee(employee_compailed_deatils,db)

  
    # #get all employees
    async def get_all_employee(self,employee_id,db:AsyncSession):
        return await self.employee_repository.fetch_all_employee_salary(employee_id,db)

    # #increament
    async def increase_salary(self, employee_id: int, increment_details, db: AsyncSession) -> EmployeePayDeatils:
        
        return await self.employee_repository.increase_salary(employee_id, increment_details.percent, db)

    #get department totals 
    async def get_department_totals(self, db: AsyncSession):
        return await self.employee_repository.fetch_department_totals(db)

#instance of the Employee Salary Service
employee_salary_service = EmployeeSalaryService() 