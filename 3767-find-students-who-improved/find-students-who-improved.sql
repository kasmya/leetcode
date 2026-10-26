with cte as (
    select 
    student_id,
    subject,
    score,
    row_number()
    over( 
        partition by student_id, subject
        order by exam_date asc 
    )
    as first_rn,
    row_number()
    over(
        partition by student_id, subject
        order by exam_date desc
    )
    as last_rn 
    from scores
)
select f.student_id, f.subject, f.score as first_score,
l.score as latest_score
from cte f
join cte l 
on f.student_id = l.student_id and f.subject = l.subject
where f.first_rn = 1 and l.last_rn = 1 and l.score > f.score
order by f.student_id, f.subject