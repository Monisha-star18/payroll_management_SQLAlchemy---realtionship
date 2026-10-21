from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.report_services import employee_report
from database import get_session

router = APIRouter(prefix="/api/report",tags=["Report"])

@router.get('/')
async def get_employee_report(db:AsyncSession = Depends(get_session)):
    return await employee_report.get_report(db)