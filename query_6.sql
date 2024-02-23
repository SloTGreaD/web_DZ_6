

SELECT s.id, s.full_name
FROM students s
WHERE s.group_id = (SELECT id FROM groups WHERE name = 'Group A')
