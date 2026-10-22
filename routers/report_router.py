from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session

from dependency.dependency import get_all_report_services
from services.report_services import EmployeeReport

router = APIRouter(prefix="/api/report",tags=["Report"])

@router.get('/')
async def get_employee_report(db:AsyncSession = Depends(get_session),
                              service : EmployeeReport = Depends(get_all_report_services)
                              ):
    return await service.get_report(db)