import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT grades.grade, students.fullname, subjects.name, groups.name
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.id = 5 AND groups.id = 1
"""

print(execute_query(sql))