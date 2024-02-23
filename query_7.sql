

SELECT s.id, s.full_name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE s.group_id = (SELECT id FROM groups WHERE name = 'Group A') 
AND sub.name = 'Physics'; 
