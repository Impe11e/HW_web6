import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT
    AVG(grades.grade) AS average_score
FROM
    students
JOIN
    grades ON students.id = grades.student_id
GROUP BY
    students.id
ORDER BY
    average_score DESC
LIMIT
    5; 
"""

print(execute_query(sql))