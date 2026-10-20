import asyncio
from database.connection import engine
from models import Base, EmployeePayDeatils,EmployeeDeatils


async def create_tables():
    async with engine.begin() as connection :
        await connection.run_sync(Base.metadata.create_all)

        print("Tables are created")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(create_tables())