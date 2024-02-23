

SELECT gr.id, gr.name, AVG(g.grade) as avg_grade
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Mathematics' 
GROUP BY gr.id;
