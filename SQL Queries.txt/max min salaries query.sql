SELECT MAX(salary) FROM employees;
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees));


SELECT salary FROM employees ORDER BY salary DESC LIMIT 1;
SELECT salary FROM employees WHERE salary < (SELECT salary FROM employees ORDER BY salary DESC LIMIT 1)  ORDER BY salary DESC LIMIT 1;
SELECT salary FROM employees WHERE salary < (SELECT salary FROM employees WHERE salary < (SELECT salary FROM employees ORDER BY salary DESC LIMIT 1)  ORDER BY salary DESC LIMIT 1)  ORDER BY salary DESC LIMIT 1;


WITH ranked_employees AS (
  SELECT 
    first_name, 
    salary, 
    RANK() OVER (
      ORDER BY 
        salary DESC
    ) AS rank 
  FROM 
    employees
) 
SELECT 
  first_name, 
  salary 
FROM 
  ranked_employees 
where 
  rank = 1;


WITH ranked_employees AS (
  SELECT 
    first_name, 
    salary, 
    RANK() OVER (
      ORDER BY 
        salary DESC
    ) AS rank 
  FROM 
    employees
) 
SELECT 
  first_name, 
  salary 
FROM 
  ranked_employees 
where 
  rank = 2;


WITH ranked_employees AS (
  SELECT 
    first_name, 
    salary, 
    RANK() OVER (
      ORDER BY 
        salary DESC
    ) AS rank 
  FROM 
    employees
) 
SELECT 
  first_name, 
  salary 
FROM 
  ranked_employees 
where 
  rank = 3;


WITH ranked_employees AS (
  SELECT 
    first_name, 
    salary, 
    RANK() OVER (
      ORDER BY 
        salary DESC
    ) AS rank 
  FROM 
    employees
) 
SELECT 
  first_name, 
  salary 
FROM 
  ranked_employees 
where 
  rank BETWEEN 1 AND 3;
