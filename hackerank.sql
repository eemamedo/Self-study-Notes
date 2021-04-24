/*------------------------------------------------------------------BASIC SELECT------------------------------------------------------------------*/

/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows: where LAT_N is the northern latitude and LONG_W is the western longitude.

For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output
ABC 3
PQRS 4

Explanation
When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

Note
You can write two separate queries to get the desired output. It need not be a single query.
*/

(
    SELECT CITY, LENGTH(CITY) AS `length`
    FROM STATION
    ORDER BY `length` ASC, CITY ASC
    LIMIT 1
) UNION (
    SELECT CITY, LENGTH(CITY) AS `length`
    FROM STATION
    ORDER BY `length` DESC, CITY ASC
    LIMIT 1
)



/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY RLIKE '^[aeiouAEIOU].*$' 
/*https://www.geeksforgeeks.org/rlike-operator-in-mysql/ - pattern*/
/*https://www.guru99.com/regular-expressions.html - examples*/
/*or can be done with bunch of like*/


/*
Query the list of CITY names ending with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY RLIKE '^*.[aeiouAEIOU]$' 

/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and 
last characters. Your result cannot contain duplicates.
*/

select CITY
from STATION
where CITY RLIKE '^[aeiouAEIOU].*[aeiouAEIOU]$'

/*
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
*/
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT RLIKE '^*.[aeiouAEIOU]$' AND CITY NOT RLIKE '^[aeiouAEIOU].*$' 


/*
Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name.
If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
*/
select name
from students
where marks>75
order by right(name, 3), ID ASC

/*
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
utput one of the following statements for each record in the table:
Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
*/

SELECT CASE WHEN A + B <= C OR B + C <= A OR A + C <= B then "Not A Triangle"
            WHEN A=B and B=C and A=C then "Equilateral"
            WHEN A=B or B=C or A=C then "Isosceles"
            ELSE "Scalene"
        end
from TRIANGLES;

/*
Generate the following two result sets:

1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter 
of each profession as a parenthetical (i.e.: enclosed in parentheses). 
For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).


2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
There are a total of [occupation_count] [occupation]s.
where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.
*/

select CONCAT(name, '(', left(occupation, 1), ')') as task_1
from occupations
order by name ASC;

select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.')
from occupations
group by occupation
order by count(occupation);

/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and 
displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

Input Format

The OCCUPATIONS table is described as follows:
*/

/*Review Again*/

/*https://stackoverflow.com/questions/38759662/not-able-to-understand-this-sql-query*/
SET @d=0, @a=0, @p=0, @s=0;
SELECT MIN(Doctor),MIN(Professor),MIN(SINGER),MIN(Actor)
FROM
(SELECT IF(OCCUPATION='Actor',NAME,NULL) AS Actor, 
        IF(OCCUPATION='Doctor',NAME,NULL) AS Doctor, 
        IF(OCCUPATION='Professor',NAME,NULL) AS Professor, 
        IF(OCCUPATION='Singer',NAME,NULL) AS SINGER,
    case OCCUPATION when 'ACTOR' THEN @a:=@a+1 
                    when 'Doctor' THEN @d:=@d+1 
                    when 'Professor' THEN @p:=@p+1 
                    when 'Singer' THEN @s:=@s+1 
    end 
    as idn FROM OCCUPATIONS ORDER BY NAME ) AS TMP GROUP BY TMP.idn ;

        
/*
Given the table schemas below, 
write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.
*/

/*REDO WITH JOINs*/

select C.Company_Code, C.founder, count(distinct(LM.lead_manager_code)), count(distinct(SM.senior_manager_code)), count(distinct(M.manager_code)), count(distinct(E.employee_code))
from company as C, Lead_Manager as LM, Senior_Manager as SM, Manager as M, Employee as E
where c.company_code = lm.company_code 
      and lm.lead_manager_code=sm.lead_manager_code
      and sm.senior_manager_code=m.senior_manager_code 
      and m.manager_code=e.manager_code
group by C.company_code, C.founder
order by C.company_code;

/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did
not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the
difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.
*/

SELECT ceiling(avg(Salary)-avg(REPLACE(Salary,0,'')))
from employees;


/*
Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. 
*/

select max(salary*months), count(salary*months) as salary_per_month 
from Employee
group by salary*months
order by salary_per_month desc
limit 1;
