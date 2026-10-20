from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from models import EmployeeDeatils , EmployeePayDeatils

class EmployeeReportRepo:

    def __init__(self):
        pass

    async def fetch_report(db:AsyncSession):
        try:
            stmt_tc = select(func.count()).select_from(EmployeeDeatils)
            result = db.execute(stmt_tc)
        except:
            pass
            

