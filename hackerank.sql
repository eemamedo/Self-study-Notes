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
