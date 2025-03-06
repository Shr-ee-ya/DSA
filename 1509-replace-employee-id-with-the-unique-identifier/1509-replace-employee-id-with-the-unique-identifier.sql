# Write your MySQL query statement below
/* select Employees.id as unique_id ,name 
from EmployeeUNI
left join Employees
on EmployeeUNI.id=Employees.id;*/

SELECT 
    EmployeeUNI.unique_id, 
    Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;

#LEFT JOIN ensures all employees are included. If no match is found in EmployeeUNI, unique_id will be NULL.