INSERT INTO employee_deatils
(employee_id, employee_name, gender, department) VALUES
(1, 'Arun', 'Male', 'IT'), (2, 'Priya', 'Female', 'HR'), (3, 'Kumar', 'Male', 'IT'),
(4, 'Divya', 'Female', 'Finance'),(5, 'Ravi', 'Male', 'HR')

INSERT INTO employee_salary
(employee_id, basic_salary, da, pf, gross_salary) VALUES
(1, 30000, 3000, 3600, 33000),(2, 25000, 2500, 3000, 27500),(3, 40000, 4000, 4800, 44000)

CREATE OR REPLACE PROCEDURE sp_increase_salary( p_employee_id INTEGER, p_percent NUMERIC )
LANGUAGE plpgsql
AS $$
DECLARE
    v_new_basic NUMERIC(12,2);
    v_da NUMERIC(12,2);
	v_pf NUMERIC(12,2);
BEGIN
    SELECT ROUND( basic_salary + (basic_salary * p_percent / 100), 2)
    INTO v_new_basic FROM employee_salary
    WHERE employee_id = p_employee_id;

    v_da := ROUND(v_new_basic * 0.10, 2);
	v_pf := ROUND(v_new_basic * 0.12, 2);

    UPDATE employee_salary
       SET basic_salary = v_new_basic,
           da = v_da,
		   pf = v_pf,
           gross_salary = v_new_basic + v_da + v_pf
     WHERE employee_id = p_employee_id;
END;
$$;