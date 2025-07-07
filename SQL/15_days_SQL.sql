select
    *
from
    (
        select
            submission_date,
            hacker_id,
            count(submission_id) as count_sub
        from
            Submissions
            -- where submission_date like '2016-03-03'
        group by
            submission_date,
            hacker_id
        order by
            submission_date,
            count_sub desc,
            hacker_id
    ) AS sub_counts_table AS