import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT AVG(grades.grade)
FROM grades
"""

print(execute_query(sql))