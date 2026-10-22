from services.payroll_services import PayrollService
from services.employee_salary_service import EmployeeSalaryService
from repositories.employee_salary_repo import EmployeeSalaryRepo

from repositories.report_repo import EmployeeReportRepo
from services.report_services import EmployeeReport

def get_all_services()->EmployeeSalaryService:

    payroll_cal = PayrollService()
    
    repository = EmployeeSalaryRepo()

    services = EmployeeSalaryService(payroll_cal,repository)

    return services 

def get_all_report_services()->EmployeeReport:

    repository = EmployeeReportRepo()

    service = EmployeeReport(repository)

    return service

