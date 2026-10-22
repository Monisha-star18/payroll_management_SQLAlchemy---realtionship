from abc import ABC,abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession


class EmployeeSalaryRepoInterface(ABC):

    @abstractmethod
    async def post_employee_personalDetails(self, employee_details: dict, db: AsyncSession):
        pass

    @abstractmethod
    async def post_employee(self, employee_details: dict, db: AsyncSession):
        pass

    @abstractmethod
    async def fetch_all_employee_salary(self, employee_id: int, db: AsyncSession):
        pass

    @abstractmethod
    async def increase_salary(self, employee_id: int, percent: float, db: AsyncSession):
        pass

    @abstractmethod
    async def fetch_department_totals(self, db: AsyncSession):
        pass
        
