-- Table groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Table students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(70) UNIQUE NOT NULL,
    group_id INTEGER REFERENCES groups(id)
    ON DELETE CASCADE
);

-- Table teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(70) UNIQUE NOT NULL
);

-- Table subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
    ON DELETE CASCADE
);

-- Table grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    date_grade DATE NOT NULL,
    student_id INTEGER REFERENCES students(id)
     ON DELETE CASCADE,
    subject_id INTEGER REFERENCES subjects(id)
     ON DELETE CASCADE
);