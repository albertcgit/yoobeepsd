import sqlite3

# Classes to represent entities

class Teacher:
    def __init__(self, number, name):
        self.teacher_id = number
        self.teacher_name = name

class Student:
    def __init__(self, number, name):
        self.student_id = number
        self.student_name = name

class Course:
    def __init__(self, code, name, teacher_id=None):
        self.course_code = code
        self.course_name = name
        self.teacher_id = teacher_id

# Class for database
class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        self.drop_tables() # I put dropping table before creating so there won't be error during re-runs
        self.create_tables()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS enrollments")
        self.cursor.execute("DROP TABLE IF EXISTS courses")
        self.cursor.execute("DROP TABLE IF EXISTS teachers")
        self.cursor.execute("DROP TABLE IF EXISTS students")
        self.connection.commit()

#Create 4 tables ( teachers, students, courses, enrollment(junction table) )

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE teachers (
                teacher_id INTEGER PRIMARY KEY,
                teacher_name TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE courses (
                course_code TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE enrollments (
                student_id INTEGER NOT NULL,
                course_code TEXT NOT NULL,
                PRIMARY KEY (student_id, course_code),
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_code) REFERENCES courses(course_code)
            )
        """)

        self.connection.commit()

#Insert functions
    def add_teacher(self, teacher):
        self.cursor.execute(
            "INSERT INTO teachers (teacher_id, teacher_name) VALUES (?, ?)",
            (teacher.teacher_id, teacher.teacher_name)
        )
        self.connection.commit()

    def add_student(self, student):
        self.cursor.execute(
            "INSERT INTO students (student_id, student_name) VALUES (?, ?)",
            (student.student_id, student.student_name)
        )
        self.connection.commit()

    def add_course(self, course):
        self.cursor.execute(
            "INSERT INTO courses (course_code, course_name, teacher_id) VALUES (?, ?, ?)",
            (course.course_code, course.course_name, course.teacher_id)
        )
        self.connection.commit()

    def enroll_student(self, student_id, course_code):
        self.cursor.execute(
            "INSERT OR IGNORE INTO enrollments (student_id, course_code) VALUES (?, ?)",
            (student_id, course_code)
        )
        self.connection.commit()

#query functions
    def get_student_count(self, course_code):
        self.cursor.execute(
            "SELECT COUNT(*) FROM enrollments WHERE course_code = ?",
            (course_code,)
        )
        return self.cursor.fetchone()[0]

    def get_teachers_for_course(self, course_code):
        self.cursor.execute("""
            SELECT t.teacher_name
            FROM teachers t
            JOIN courses c ON t.teacher_id = c.teacher_id
            WHERE c.course_code = ?
        """, (course_code,))
        return [row[0] for row in self.cursor.fetchall()]

    def get_students_in_course(self, course_code):
        self.cursor.execute("""
            SELECT s.student_id, s.student_name
            FROM students s
            JOIN enrollments e ON s.student_id = e.student_id
            WHERE e.course_code = ?
        """, (course_code,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    db = Database("W3A4_database_file.db") #Create my database object

    teacher1 = Teacher(1, "Mohammed")
    teacher2 = Teacher(2, "Arun")
    teacher3 = Teacher(3, "Saveeta")

    student1 = Student(1, "Albert")
    student2 = Student(2, "Earl")
    student3 = Student(3, "Roxy")
    student4 = Student(4, "Benj")

    course1 = Course("MSE800", "Professional Software Engineering", 1)
    course2 = Course("MSE801", "Research Methods", 2)
    course3 = Course("MSE802", "Quantum Computing", 3)

    # Insert data
    db.add_teacher(teacher1)
    db.add_teacher(teacher2)
    db.add_teacher(teacher3)

    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)
    db.add_student(student4)

    db.add_course(course1)
    db.add_course(course2)
    db.add_course(course3)

    # Enrollments
    db.enroll_student(1, "MSE800")

    db.enroll_student(1, "MSE801")
    db.enroll_student(2, "MSE801")

    db.enroll_student(1, "MSE802")
    db.enroll_student(2, "MSE802")
    db.enroll_student(3, "MSE802")
    db.enroll_student(4, "MSE802")

    student_count = db.get_student_count("MSE800")
    print(f"The number of students enrolled in MSE800 is {student_count}.")

    teachers_MSE801 = db.get_teachers_for_course("MSE801")
    print(f"Teachers teaching MSE801: {teachers_MSE801}")

    db.close()