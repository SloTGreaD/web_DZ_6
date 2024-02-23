

SELECT sub.id, sub.name
FROM subjects sub
WHERE sub.teacher_id = (SELECT id FROM teachers WHERE full_name = 'Mark Gonzales') 
