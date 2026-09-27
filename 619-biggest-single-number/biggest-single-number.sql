select max(distinct num) as num from mynumbers 
where num in (
    select max(num) from mynumbers group by num having count(*)<=1
)