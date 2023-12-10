import logging
import random
import sqlite3
from sqlite3 import DatabaseError

import faker

conn = sqlite3.connect('homework1.db')
cur = conn.cursor()

fake = faker.Faker()

# groups
for _ in range(3):
    cur.execute('INSERT INTO groups (name) VALUES (?)', (fake.word(),))

# teachers
for _ in range(4):
    cur.execute('INSERT INTO teachers (fullname) VALUES (?)', (fake.name(),))

# subjects
for _ in range(5):
    cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (fake.word(), random.randint(1, 4)))


# students with grades
for group_id in range(1, 4):
    for _ in range(15):
        cur.execute('INSERT INTO students (fullname, group_id) VALUES (?, ?)',
                    (fake.name(), group_id))
        student_id = cur.lastrowid
        for subject_id in range(1, 10):
            cur.execute('INSERT INTO grades (grade, date_grade, student_id, subject_id) VALUES (?, ?, ?, ?)',
                        (random.randint(1, 100), fake.date_this_decade(), student_id, subject_id))

try:
    conn.commit()
except DatabaseError as err:
    logging.error(err)
    conn.rollback()
finally:
    cur.close()
    conn.close()
