
class PayrollService:
    
    @staticmethod
    def calculate_da(basic_salary):
        return round(basic_salary * 0.10,2)
    
    @staticmethod
    def calculate_pf(basic_salary):
        return round(basic_salary * 0.12,2)

    @staticmethod
    def calculate_gross_salary(basic_salary):
        da = PayrollService.calculate_da(basic_salary)
        return round(basic_salary + da,2)