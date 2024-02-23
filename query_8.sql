

SELECT t.id, t.full_name, AVG(g.grade) as avg_grade
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN grades g ON sub.id = g.subject_id
WHERE t.full_name = 'Mark Gonzales' 