import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('homework1.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT students.fullname
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.id = 3
"""

print(execute_query(sql))