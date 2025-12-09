import mysql.connector as mysql
import dotenv
import csv
import os


dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")


db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

with open(csv_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)

    for row in file_data:
        name = row['name']
        second_name = row['second_name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        query = """
        SELECT
            st.name,
            st.second_name,
            gr.title as group_title,
            b.title as book_title,
            sub.title as subject_title,
            l.title as lesson_title,
            m.value as mark_value
        FROM students st
        JOIN `groups` gr ON st.group_id = gr.id
        JOIN books b ON b.taken_by_student_id = st.id
        JOIN marks m ON m.student_id = st.id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects sub ON l.subject_id = sub.id
        WHERE st.name = %s
            AND st.second_name = %s
            AND gr.title = %s
            AND b.title = %s
            AND sub.title = %s
            AND l.title = %s
            AND m.value = %s
            """

        cursor.execute(
            query, (
                name,
                second_name,
                group_title,
                book_title,
                subject_title,
                lesson_title,
                mark_value
            )
        )

        result = cursor.fetchall()

        if not result:
            print("Data not exist in Database:")
            print(f"  Student: {name} {second_name}")
            print(f"  Groups: {group_title}")
            print(f"  Books: {book_title}")
            print(f"  Subjects: {subject_title}")
            print(f"  Lessons: {lesson_title}")
            print(f"  Marks: {mark_value}")


cursor.close()
db.close()
