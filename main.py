from faker import Faker
import sqlite3



fake = Faker()


conn = sqlite3.connect('lesson.sqlite')
cursor = conn.cursor()


groups = ['A', 'B', 'C']
for i, group in enumerate(groups, start=1):
    cursor.execute('INSERT INTO groups (id, name) VALUES (?, ?)', (i, f'Group {group}'))

# Insert teachers
for _ in range(5):
    cursor.execute('INSERT INTO teachers (full_name) VALUES (?)', (fake.name(),))


# Insert subjects with random teachers
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Art', 'Physical Education']
for i, subject in enumerate(subjects, start=1):
    teacher_id = fake.random_int(min=1, max=5)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

# Insert students and grades
for i in range(50):
    group_id = fake.random_int(min=1, max=3)
    cursor.execute('INSERT INTO students (full_name, group_id) VALUES (?, ?)', (fake.name(), group_id))
    student_id = cursor.lastrowid
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(fake.random_int(min=5, max=20)):  # Each student gets 5-20 grades per subject
            grade = fake.random_int(min=1, max=100)
            date_received = fake.date_between(start_date='-2y', end_date='today').isoformat()
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date_received))


# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()