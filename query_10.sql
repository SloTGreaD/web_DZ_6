

SELECT sub.id, sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.student_id = (SELECT id FROM students WHERE full_name = 'Jennifer Carroll') 
AND sub.teacher_id = (SELECT id FROM teachers WHERE full_name = 'Alexis Carey'); 