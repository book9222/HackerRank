select
    months * salary as total_slr,
    count(*)
from
    Employee
where
    (
        select
            max(months * salary) as max_total_slr
        from
            Employee
    ) = months * salary
group by
    total_slr