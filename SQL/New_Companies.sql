select C.company_code, C.founder, 
count(distinct LM.lead_manager_code), 
count(distinct SM.senior_manager_code), 
count(distinct M.manager_code), 
count(distinct E.employee_code) 
from Company C 
left join Lead_Manager LM on C.company_code  = LM.company_code 
left join Senior_Manager SM on C.company_code = SM.company_code
left join Manager M on C.company_code = M.company_code
left join Employee E on C.company_code = E.company_code
GROUP BY C.company_code, C.founder
order by C.company_code
