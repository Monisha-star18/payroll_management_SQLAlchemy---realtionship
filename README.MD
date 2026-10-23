# Employee Payroll Management API

### Install

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure the environment

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=payroll_management_db
DB_USER=postgres
DB_PASSWORD=your_password

DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

The app stops at start-up with an error if `DATABASE_URL` is not set. Create the empty database first:

```sql
CREATE DATABASE payroll_management_db;
```

### 4. Run the migrations

From the project root:

```bash
alembic upgrade head
```

This creates the tables, inserts the sample employee and salary data, and creates the `sp_increase_salary` stored procedure.

### 5. Start the server

```bash
uvicorn app.main:app --reload
```
