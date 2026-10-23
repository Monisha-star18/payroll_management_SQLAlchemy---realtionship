from fastapi import FastAPI

from routers.employee_salary_router import router as employee_salary_router
from routers.report_router import router as report_router

app=FastAPI(title="Employee Payroll Management")

app.include_router(employee_salary_router)
app.include_router(report_router)
