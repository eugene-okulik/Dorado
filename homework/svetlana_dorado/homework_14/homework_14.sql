-- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
-- 1. Создайте студента (student)
INSERT INTO students (name, second_name, group_id) VALUES ('Svetlana', 'Dorado', NULL);

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('Think Python: How to Think Like a Computer Scientist', 21767);

-- 3. Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group for Dorado', 'September 2025', 'January 2026');

UPDATE students SET group_id = 21589 WHERE name = 'Svetlana' AND second_name = 'Dorado';

-- 4. Создайте несколько учебных предметов (subjects)
INSERT INTO subjects (title) VALUES 
('History of Rock and Roll'),
('Cybersecurity and Cyber Warfare');

-- 5. Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES 
('Origins & Blues Roots', 13061),
('Elvis & The 50s', 13061),
('Cryptography Basics', 13062),
('Incident Response', 13062);

-- 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
SELECT * FROM lessons WHERE subject_id IN (13061, 13062);

INSERT INTO marks (value, lesson_id, student_id) VALUES
(5, 73532, 21767), 
(4, 73533, 21767), 
(5, 73534, 21767), 
(4, 73535, 21767);

-- Получите информацию из базы данных:
-- 1. Все оценки студента
SELECT value FROM marks WHERE student_id = 21767;

-- 2. Все книги, которые находятся у студента
SELECT title FROM books WHERE taken_by_student_id = 21767;

-- 3. Для вашего студента выведите всё, что о нем есть в базе:
-- группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
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
WHERE s.id = 21767
