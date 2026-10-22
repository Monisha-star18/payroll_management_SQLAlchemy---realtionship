from sqlalchemy.ext.asyncio import AsyncSession

from repositories.report_repo_interface import EmployeeReportRepoInterface

class EmployeeReport:

        def __init__(self,report_repo:EmployeeReportRepoInterface):
                self.report_repo=report_repo

        async def get_report(self,db:AsyncSession):
                return await  self.report_repo.fetch_report(db)

