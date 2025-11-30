import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

# 1. Создать студента (student)
query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s);"
values = ("Vladislav", "Winner", None)
cursor.execute(query, values)
student_id = cursor.lastrowid

query = "SELECT * FROM students WHERE id = %s"
values = (student_id,)
cursor.execute(query, values)

new_student = cursor.fetchone()
print(f"Student created: {new_student}")

# 2. Создать несколько книг (books) и указать, что созданный студент взял их
many_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s);"
cursor.executemany(
    many_query, [
        ("Book one for Vladislav Winner", student_id),
        ("Book two for Vladislav Winner", student_id)
    ]
)

query = '''
SELECT *
FROM books
WHERE taken_by_student_id = %s
ORDER BY id DESC
LIMIT 2
'''

cursor.execute(query, (student_id,))
new_books = cursor.fetchall()
print(f"Books created: {new_books}")

# 3.1 Создать группу (group)
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s);"
values = ("Group for Winner", "September 2025", "January 2026")
cursor.execute(query, values)
group_id = cursor.lastrowid

query = "SELECT * FROM `groups` WHERE id = %s"
values = (group_id,)
cursor.execute(query, values)

new_group = cursor.fetchone()
print(f"Group created: {new_group}")

# 3.2 Oпределить студента в группу
query = "UPDATE students SET group_id = %s WHERE id = %s;"
values = (group_id, student_id)
cursor.execute(query, values)

query = "SELECT * FROM students WHERE id = %s"
values = (student_id,)
cursor.execute(query, values)

new_student = cursor.fetchone()
print(f"Student updated: {new_student}")

# 4. Создать несколько учебных предметов (subjects)
query = "INSERT INTO subjects (title) VALUES (%s);"
cursor.execute(query, ("Subject one for Vladislav Winner",))
subject_one_id = cursor.lastrowid

query = "INSERT INTO subjects (title) VALUES (%s);"
cursor.execute(query, ("Subject two for Vladislav Winner",))
subject_two_id = cursor.lastrowid

query = '''
SELECT *
FROM subjects
WHERE id IN (%s, %s)
ORDER BY id DESC
'''

cursor.execute(query, (subject_one_id, subject_two_id))
new_subjects = cursor.fetchall()
print(f"Subjects created: {new_subjects}")

# 5. Создать по два занятия для каждого предмета (lessons)
many_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s);"
cursor.executemany(
    many_query, [
        ("Lesson one for subject one", subject_one_id),
        ("Lesson two for subject one", subject_one_id),
        ("Lesson one for subject two", subject_two_id),
        ("Lesson two for subject two", subject_two_id)
    ]
)

query = '''
SELECT *
FROM lessons
WHERE subject_id IN (%s, %s)
ORDER BY subject_id, id
'''

cursor.execute(query, (subject_one_id, subject_two_id))
new_lessons = cursor.fetchall()
print(f"Lessons created: {new_lessons}")

# 6. Поставить студенту оценки (marks) для всех созданных занятий
marks = [5, 4, 3, 5]
marks_data = []

for lesson, mark in zip(new_lessons, marks):
    lesson_id = lesson["id"]
    marks_data.append((mark, lesson_id, student_id))

many_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s);"
cursor.executemany(many_query, marks_data)

query = '''
SELECT *
FROM marks
WHERE student_id = %s
ORDER BY id DESC
LIMIT 4
'''

cursor.execute(query, (student_id,))
new_marks = cursor.fetchall()
print(f"Marks set: {new_marks}")

# 7. Получить все оценки студента
query = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query, (student_id,))
student_marks = cursor.fetchall()
print(f"Student's marks gotten: {student_marks}")

# 8. Получить все книги, которые находятся у студента
query = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query, (student_id,))
student_books = cursor.fetchall()
print(f"Student's books gotten: {student_books}")

# 9. Получить всё что есть в базе о студенте с использованием Join
query = '''
SELECT
    s.name,
    s.second_name,
    g.title AS group_name,
    b.title AS book_taken,
    m.value AS mark,
    l.title AS lesson_name,
    sub.title AS subject_name
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
'''

cursor.execute(query, (student_id,))
student_full_info = cursor.fetchall()
print(f"Student's full information gotten: {student_full_info}")

db.commit()

db.close()
