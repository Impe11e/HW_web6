import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id 
WHERE students.id = 5 AND teachers.id = 1
"""

print(execute_query(sql))