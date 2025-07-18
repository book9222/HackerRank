select
    sum(ci.population)
from
    city ci
    left join country co on ci.CountryCode = co.Code
where
    co.continent = 'Asia'
    -- group by co.continent