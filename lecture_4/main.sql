-- SQL query number 1

Create TABLE students (
          id integer ,
          full_name text,
          birth_year integer);

-- SQL query number 2

Create TABLE grades (
          id INTEGER,
          student_id integer,
          subject text,
          grade integer);

-- SQL query number 3

INSERT INTO students (id, full_name, birth_year) VALUES (1, 'Alice Johnson', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (2, 'Brian Smith', 2004);
INSERT INTO students (id, full_name, birth_year) VALUES (3, 'Carla Reyes', 2006);
INSERT INTO students (id, full_name, birth_year) VALUES (4, 'Daniel Kim', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (5, 'Eva Thompson', 2003);
INSERT INTO students (id, full_name, birth_year) VALUES (6, 'Felix Nguyen', 2007);
INSERT INTO students (id, full_name, birth_year) VALUES (7, 'Grace Patel', 2005);
INSERT INTO students (id, full_name, birth_year) VALUES (8, 'Henry Lopez', 2004);
INSERT INTO students (id, full_name, birth_year) VALUES (9, 'Isabella Martinez', 2006);


INSERT INTO grades (id, student_id, subject, grade) VALUES (1, 1, 'Math', 88);
INSERT INTO grades (id, student_id, subject, grade) VALUES (2, 1, 'English', 92);
INSERT INTO grades (id, student_id, subject, grade) VALUES (3, 1, 'Science', 85);
INSERT INTO grades (id, student_id, subject, grade) VALUES (4, 2, 'Math', 75);
INSERT INTO grades (id, student_id, subject, grade) VALUES (5, 2, 'History', 83);
INSERT INTO grades (id, student_id, subject, grade) VALUES (6, 2, 'English', 79);
INSERT INTO grades (id, student_id, subject, grade) VALUES (7, 3, 'Science', 95);
INSERT INTO grades (id, student_id, subject, grade) VALUES (8, 3, 'Math', 91);
INSERT INTO grades (id, student_id, subject, grade) VALUES (9, 3, 'Art', 89);
INSERT INTO grades (id, student_id, subject, grade) VALUES (10, 4, 'Math', 84);
INSERT INTO grades (id, student_id, subject, grade) VALUES (11, 4, 'Physical Education', 93);
INSERT INTO grades (id, student_id, subject, grade) VALUES (12, 5, 'English', 90);
INSERT INTO grades (id, student_id, subject, grade) VALUES (13, 4, 'Science', 88);
INSERT INTO grades (id, student_id, subject, grade) VALUES (14, 5, 'History', 85);
INSERT INTO grades (id, student_id, subject, grade) VALUES (15, 5, 'Math', 88);
INSERT INTO grades (id, student_id, subject, grade) VALUES (16, 6, 'Science', 72);
INSERT INTO grades (id, student_id, subject, grade) VALUES (17, 6, 'Math', 78);
INSERT INTO grades (id, student_id, subject, grade) VALUES (18, 6, 'English', 81);
INSERT INTO grades (id, student_id, subject, grade) VALUES (19, 7, 'Art', 94);
INSERT INTO grades (id, student_id, subject, grade) VALUES (20, 7, 'Science', 87);
INSERT INTO grades (id, student_id, subject, grade) VALUES (21, 7, 'Math', 90);
INSERT INTO grades (id, student_id, subject, grade) VALUES (22, 8, 'History', 77);
INSERT INTO grades (id, student_id, subject, grade) VALUES (23, 8, 'Math', 83);
INSERT INTO grades (id, student_id, subject, grade) VALUES (24, 8, 'Science', 80);
INSERT INTO grades (id, student_id, subject, grade) VALUES (25, 9, 'English', 96);
INSERT INTO grades (id, student_id, subject, grade) VALUES (26, 9, 'Math', 89);
INSERT INTO grades (id, student_id, subject, grade) VALUES (27, 9, 'Art', 92);

-- SQL query number 4

SELECT grade FROM grades INNER JOIN students ON grades.student_id = students.id where students.id = 1;

-- SQL query number 5

SELECT full_name, ROUND(AVG(grade), 2) FROM students JOIN grades ON students.id = grades.student_id GROUP BY students.id, full_name;

-- SQL query number 6

SELECT * FROM students where birth_year > 2004;

-- SQL query number 7

SELECT subject, ROUND(AVG(grade), 2) FROM grades GROUP BY subject;

-- SQL query number 8

SELECT full_name, ROUND(AVG(grade), 2) as avg_gr FROM students JOIN grades ON students.id = grades.student_id GROUP BY students.id, full_name ORDER BY avg_gr DESC LIMIT 3;

-- SQL query number 9

SELECT full_name FROM students JOIN grades ON students.id = grades.student_id WHERE grade < 80 GROUP BY students.id, full_name;