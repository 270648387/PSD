PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS student (
    student_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name  TEXT NOT NULL,
    address       TEXT
);

CREATE TABLE IF NOT EXISTS class (
    class_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    description   TEXT
);

CREATE TABLE IF NOT EXISTS lecturer (
    lecturer_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    lect_name     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS subject (
    subject_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name  TEXT NOT NULL,
    class_id      INTEGER NOT NULL,
    lecturer_id   INTEGER,
    FOREIGN KEY (class_id) REFERENCES class(class_id),
    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id)
);

CREATE TABLE IF NOT EXISTS student_class (
    student_id  INTEGER NOT NULL,
    class_id    INTEGER NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (class_id)   REFERENCES class(class_id)
);

CREATE TABLE IF NOT EXISTS student_subject (
    student_id  INTEGER NOT NULL,
    subject_id  INTEGER NOT NULL,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id)
);

CREATE TABLE IF NOT EXISTS lecturer_class (
    lecturer_id  INTEGER NOT NULL,
    class_id     INTEGER NOT NULL,
    PRIMARY KEY (lecturer_id, class_id),
    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
    FOREIGN KEY (class_id)    REFERENCES class(class_id)
);
