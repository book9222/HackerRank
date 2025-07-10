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
    -- select
    --     max(total_slr) as max_total_slr,
    --     count(total_slr) as c_total_slr
    -- from
    --     (
    --         select
    --             months * salary as total_slr
    --         from
    --             Employee
    --     ) as total_slr_table
    -- group by
    --     total_slr