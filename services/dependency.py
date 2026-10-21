from payroll_services import PayrollService
from services.employee_salary_service import EmployeeSalaryService

def get_service() :
   
    payroll_cal = PayrollService()

    payroll_service = EmployeeSalaryService(payroll_cal)

    return payroll_service
