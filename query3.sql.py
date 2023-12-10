import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT AVG(grades.grade) as score, groups.name as gn
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE groups.id = 2
ORDER BY score
"""

print(execute_query(sql))