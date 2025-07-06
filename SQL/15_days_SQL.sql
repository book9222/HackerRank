select
    *
from
    (
        select
            S.submission_date,
            S.hacker_id,
            count(S.submission_id) as sub_count
        from
            Submissions
        group by
            submission_date,
            hacker_id
        order by
            submission_date,
            hacker_id
    ) as sub_counts_table