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