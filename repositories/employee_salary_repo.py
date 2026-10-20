from decimal import Decimal
from fastapi import HTTPException,Depends
from sqlalchemy import select,text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import joinedload

from models import EmployeePayDeatils,EmployeeDeatils

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    # #update employee
    # async def put_employee(self,employee_details,db:AsyncSession):
    #     try:
    #         employee = await db.get(EmployeePayDeatils,employee_details["employee_id"])

    #         if not employee :
    #             return {"message":f"The id {employee_details["employee_id"]} dont exists "}

    #         for column , value in employee_details.items():
    #             if column != "employee_id":
    #                 setattr(employee,column,value)

    #         await db.commit()
    #         await db.refresh(employee)

    #         return{"message":f"Employee with ID {employee_details["employee_id"]} is updated" , 
    #                            "Salary_deatiles": employee_details}
        

    #     except SQLAlchemyError as er:
    #         await db.rollback()
    #         raise HTTPException(status_code=500, detail=str(er))

    # #delete the employee 
    # async def delete_employee(self,employee_id: int,db : AsyncSession):
    #     try:
    #         employee = await db.get(EmployeePayDeatils,employee_id)
            
    #         if not employee :
    #             return {"message":f"The id {employee_id} dont exists "}

    #         await db.delete(employee)
    #         await db.commit()

    #         return{"message":f"Employee with ID {employee_id} is deleted"}

    #     except SQLAlchemyError as er:
    #         await db.rollback()
    #         raise HTTPException(status_code=500, detail=str(er))

   
    async def post_employee_personalDetails(self,employee_personal_details,db:AsyncSession):
        try:
            employee_details = employee_personal_details.model_dump()

            employee_personal_data = EmployeeDeatils(**employee_details)

            db.add(employee_personal_data)
            await db.commit()

            return{"message":f"Employee with ID {employee_details["employee_id"]} is added" , 
                    "Employee_details":employee_details}

        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=500, detail="Employee ID already exists")
        
        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))

    #create new employess
    async def post_employee(self,employee_details,db:AsyncSession):
        try:
            employee_data = EmployeePayDeatils(**employee_details)
            db.add(employee_data)
            await db.commit()

            return{"message":f"Employee with ID {employee_details["employee_id"]} is added" , 
                   "Salary_deatiles":employee_details}
       
        except IntegrityError as er:
            await db.rollback()
            
            #getattr(obj, "name", default) reads an attribute by name and returns default instead of raising AttributeError if it doesn’t exist
            #psycopg2-> pgcode
            #asyncpg->sqlstate

            code = getattr(er.orig, "sqlstate", None) or getattr(er.orig, "pgcode", None)

            if code == "23503": #Foreign key violation
                raise HTTPException(status_code=404, detail="Employee is not registered.")
            
            if code == "23505":#Primary key violation
                raise HTTPException(status_code=409, detail="Salary details already exist.")
            raise HTTPException(status_code=400, detail=str(er))


        
        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))
            

  # #get alll employees 
    async def fetch_all_employee_salary(self,employee_id,db:AsyncSession):
        try:
            employee =await db.get(EmployeeDeatils,employee_id, 
                                   options=[joinedload(EmployeeDeatils.salary)]
                                )
            
            if employee is None :
                raise HTTPException(status_code=404,
                                detail=f"Employee {employee_id} not found")
            basic = None
            gross_salary = None

            if employee.salary is not None:
                basic = employee.salary.basic_salary
                da = employee.salary.da
                pf=employee.salary.pf
                gross_salary = employee.salary.gross_salary 


            employee_deatils = {
                "employee_id": employee.employee_id,
                "employee_name": employee.employee_name,
                "gender": employee.gender,
            }

            employee_salary_details = {
                "employee_salary":basic,
                "da":da,
                "pf":pf,
                "employee_gross_salary":gross_salary
            }

            return {**employee_deatils,**employee_salary_details}

            
        except SQLAlchemyError as er:
            raise HTTPException(status_code=500, detail=str(er))

 #Increment by percentage 
    async def increase_salary(self, employee_id: int, percent: float, db: AsyncSession):
        try:
            employee = await db.get(EmployeePayDeatils, employee_id)

            if employee is None:
                return {"message":f"The id {employee_id} dont exists "}  
                           

            await db.execute(
                text("CALL sp_increase_salary(:employee_id, :percent)"),
                {"employee_id": employee_id, "percent": Decimal(str(percent))},
            )

            await db.commit()
            await db.refresh(employee)                   
            return {"message":"Increment updates","details":employee}

        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))

        
