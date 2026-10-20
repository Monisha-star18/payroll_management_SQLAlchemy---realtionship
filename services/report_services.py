from sqlalchemy.ext.asyncio import AsyncSession

from repositories.report_repo import EmployeeReportRepo

class EmployeeReport:
        def __init__(self):
                self.report_repo=EmployeeReportRepo()

        async def get_report(self,db:AsyncSession):
                return await  self.report_repo.fetch_report(db)

employee_report=EmployeeReport()