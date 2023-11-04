/*

Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of  decimal places.
The sum of all values in LONG_W rounded to a scale of  decimal places.

Output Format

Your results must be in the form:

lat lon

where lat is the sum of all values in LAT_N and lon is the sum of all values in LONG_W. 
Both results must be rounded to a scale of 2 decimal places.


*/

-- The code is run with the MySql
SELECT 
    ROUND(SUM(S.LAT_N), 2) AS northern_latitude,
    ROUND(SUM(S.LONG_W), 2) AS western_longitude
FROM
    STATION AS S;