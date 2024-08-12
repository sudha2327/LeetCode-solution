Select m.employee_id,m.name,Count(n.reports_to) as reports_count,
round(avg(n.age)) as average_age from employees m inner join employees n
on (m.employee_id=n.reports_to) group by 1 order by 1;