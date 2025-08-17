-- ======================
-- Core entities
-- ======================

CREATE TABLE student (
  student_id    INTEGER PRIMARY KEY,
  student_name  VARCHAR(120) NOT NULL,
  address       VARCHAR(200)
);

CREATE TABLE class (
  class_id      INTEGER PRIMARY KEY,
  description   VARCHAR(200)
);

CREATE TABLE lecturer (
  lecturer_id   INTEGER PRIMARY KEY,
  lect_name     VARCHAR(120) NOT NULL
);

CREATE TABLE subject (
  subject_id    INTEGER PRIMARY KEY,
  subject_name  VARCHAR(120) NOT NULL,
  -- From diagram: CLASS 1 --- M SUBJECTS  (a class has many subjects)
  class_id      INTEGER NOT NULL,
  lecturer_id   INTEGER,                -- One lecturer teaches a subject (per the picture)
  CONSTRAINT fk_subject_class
    FOREIGN KEY (class_id) REFERENCES class(class_id) ON DELETE CASCADE,
  CONSTRAINT fk_subject_lecturer
    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id) ON DELETE SET NULL
);

-- ======================
-- Relationship tables
-- ======================

-- STUDENT M:N CLASS (Attends)
CREATE TABLE student_class (
  student_id  INTEGER NOT NULL,
  class_id    INTEGER NOT NULL,
  PRIMARY KEY (student_id, class_id),
  CONSTRAINT fk_sc_student
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
  CONSTRAINT fk_sc_class
    FOREIGN KEY (class_id)   REFERENCES class(class_id)   ON DELETE CASCADE
);

-- STUDENT M:N SUBJECT (Takes)
CREATE TABLE student_subject (
  student_id  INTEGER NOT NULL,
  subject_id  INTEGER NOT NULL,
  PRIMARY KEY (student_id, subject_id),
  CONSTRAINT fk_ss_student
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
  CONSTRAINT fk_ss_subject
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
);

-- LECTURER M:N CLASS (Teaches)
-- (Allows team-teaching and historical changes.)
CREATE TABLE lecturer_class (
  lecturer_id  INTEGER NOT NULL,
  class_id     INTEGER NOT NULL,
  PRIMARY KEY (lecturer_id, class_id),
  CONSTRAINT fk_lc_lecturer
    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id) ON DELETE CASCADE,
  CONSTRAINT fk_lc_class
    FOREIGN KEY (class_id)    REFERENCES class(class_id)       ON DELETE CASCADE
);

-- Helpful indexes
CREATE INDEX ix_subject_class     ON subject(class_id);
CREATE INDEX ix_subject_lecturer  ON subject(lecturer_id);
CREATE INDEX ix_sc_student        ON student_class(student_id);
CREATE INDEX ix_sc_class          ON student_class(class_id);
CREATE INDEX ix_ss_student        ON student_subject(student_id);
CREATE INDEX ix_ss_subject        ON student_subject(subject_id);
CREATE INDEX ix_lc_lecturer       ON lecturer_class(lecturer_id);
CREATE INDEX ix_lc_class          ON lecturer_class(class_id);
