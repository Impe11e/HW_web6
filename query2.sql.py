import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT AVG(grades.grade) as score, students.fullname, su.name
FROM students
JOIN grades on students.id = grades.student_id
JOIN subjects as su ON grades.student_id = su.id
WHERE subject_id = 5
ORDER BY score DESC
LIMIT 1
"""

print(execute_query(sql))