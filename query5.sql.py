import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT subjects.name
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
WHERE teachers.id = 3
"""
print(execute_query(sql))