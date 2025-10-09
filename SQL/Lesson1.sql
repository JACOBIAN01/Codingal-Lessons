CREATE TABLE IF NOT EXISTS students(
student_id INT PRIMARY KEY ,
name VARCHAR(40) ,
gender VARCHAR(1),
grade INT
);

INSERT INTO students (student_id , name , gender , grade)
VALUES
(1,"Hareshan","M",6),
(2,"Rahul","M",6),
(3,"Sree","F",6)

SELECT * FROM students;