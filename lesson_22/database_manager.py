from peewee import fn
from database import db, Students, Course, CourseStudents


class DatabaseManager:
    def __init__(self):
        self.db = db

    def connect(self):
        if self.db.is_closed():
            self.db.connect()

    def close(self):
        if not self.db.is_closed():
            self.db.close()

    def add_student(self, **kwargs):
        self.connect()
        new_account = Students.create(**kwargs)
        self.close()
        return new_account

    def add_course(self, **kwargs):
        self.connect()
        new_account = Course.create(**kwargs)
        self.close()
        return new_account

    def get_all_students(self):
        self.connect()
        query = Students.select()
        student = []
        for result in query:
            student.append({
                'student_email': result.email,
                'first_name': result.first_name,
                'last_name': result.last_name,
            })
        self.close()
        return student

    def get_all_courses(self):
        self.connect()
        query = Course.select()
        courses = []
        for result in query:
            courses.append(result.course_name)
        self.close()
        return courses

    def add_student_to_course(self, student_email, course_name):
        self.connect()
        CourseStudents.create(student=student_email, course=course_name)
        self.close()

    def get_all_students_for_course(self, course_name):
        self.connect()
        query = (Students
                 .select(Students.email, Students.first_name, Students.last_name)
                 .join(CourseStudents, on=(Students.email == CourseStudents.student))
                 .join(Course, on=(CourseStudents.course == Course.course_name))
                 .where(Course.course_name == course_name))

        students = []
        for result in query:
            students.append({
                'student_email': result.email,
                'first_name': result.first_name,
                'last_name': result.last_name
            })

        self.close()
        return students

    def get_student_with_courses(self, email):
        self.connect()
        query = (Students
                 .select(Course.course_name)
                 .join(CourseStudents, on=(Students.email == CourseStudents.student))
                 .join(Course, on=(CourseStudents.course == Course.course_name))
                 .where(Students.email == email))
        print(query)
        student_courses = []
        for result in query:
            student_courses.append(result.coursestudents.course.course_name)

        self.close()
        return student_courses

    def update_student(self, **kwargs):
        self.connect()

        # Оновлення даних студента
        query = (Students
                 .update(**kwargs)
                 .where(Students.email == kwargs['email']))

        updated_rows = query.execute()
        self.close()

        return updated_rows

    def delete_student(self, email):
        self.connect()
        query = Students.delete().where(Students.email == email)
        deleted_rows = query.execute()
        self.close()
        return deleted_rows

    def delete_course(self, course_name):
        self.connect()
        query = Course.delete().where(Course.course_name == course_name)
        deleted_rows = query.execute()
        self.close()
        return deleted_rows
