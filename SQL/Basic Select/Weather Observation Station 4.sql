-- github.com/arpitran

/*
Enter your query here.
*/

SELECT 
    COUNT(*) - COUNT(DISTINCT CITY) 
FROM 
    STATION;
