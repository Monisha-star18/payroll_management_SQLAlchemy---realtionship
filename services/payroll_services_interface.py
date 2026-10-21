from abc import ABC,abstractmethod

class PayrollServiceInterface(ABC):

    @abstractmethod
    def calculate_da(basic_salary):
        pass    

    @abstractmethod
    def calculate_pf(basic_salary):
        pass

    @abstractmethod
    def calculate_gross_salary(basic_salary):
        pass