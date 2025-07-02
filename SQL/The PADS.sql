/*
Enter your query here.
*/

select
concat(name,'(',SUBSTRING(OCCUPATION,1,1),')')
from OCCUPATIONS
order by name asc;

select 
concat('There are a total of ',count(name),' ',lower(OCCUPATION),'s.')
from OCCUPATIONS 
group by OCCUPATION
order by count(name);