from abc import ABC,abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class EmployeeReportRepoInterface(ABC):

    @abstractmethod
    async def fetch_report(self,db:AsyncSession):
       pass

