SELECT 
  MAX(CASE WHEN occupation = 'Doctor' THEN name ELSE NULL END) AS Doctor,
  MAX(CASE WHEN occupation = 'Professor' THEN name ELSE NULL END) AS Professor,
  MAX(CASE WHEN occupation = 'Singer' THEN name ELSE NULL END) AS Singer,
  MAX(CASE WHEN occupation = 'Actor' THEN name ELSE NULL END) AS Actor
FROM (
    SELECT ROW_NUMBER() OVER(PARTITION BY Occupation order by name) as rn,
    name ,
    occupation
    FROM Occupations
  ) as occupation_row
group by rn

-- The GROUP BY in the outer query is needed because you want to combine (group) all people with the same row number (rn) from each occupation into a single row.

-- SELECT ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY name) as rn,
-- name ,
-- occupation
-- FROM Occupations

-- Create a table of row numbers for each occupation
-- - PARTITION BY Occupation: Divides the result set into groups by the Occupation column.
-- - ORDER BY name: Within each group, rows are ordered by the name column.
-- - ROW_NUMBER(): Assigns a unique number to each row within its group, starting from 1.
-- 1 Eve Actor
-- 2 Jennifer Actor
-- 3 Ketty Actor
-- 4 Samantha Actor
-- 1 Aamina Doctor
-- 2 Julia Doctor
-- 3 Priya Doctor
-- 1 Ashley Professor
-- 2 Belvet Professor
-- 3 Britney Professor
-- 4 Maria Professor
-- 5 Meera Professor
-- 6 Naomi Professor
-- 7 Priyanka Professor
-- 1 Christeen Singer
-- 2 Jane Singer
-- 3 Jenny Singer
-- 4 Kristeen Singer