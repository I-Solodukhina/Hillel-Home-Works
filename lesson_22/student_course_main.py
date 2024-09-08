from database_manager import DatabaseManager
import faker
import random

db = DatabaseManager()


def add_courses():
    courses = ['Python Pro', 'Python Basic', 'SMM', 'Frontend basic', 'Digital Marketing']
    for course_name in courses:
        db.add_course(course_name=course_name)


def add_students():
    for _ in range(20):
        first_name = faker.Faker().first_name()
        last_name = faker.Faker().last_name()
        email = faker.Faker().email()
        db.add_student(first_name=first_name, last_name=last_name, email=email)


def add_student_to_course():
    for student in db.get_all_students():
        all_courses = db.get_all_courses()
        print(student, all_courses)
        random_courses = random.sample(all_courses, k=random.randrange(len(all_courses)))
        for course in random_courses:
            db.add_student_to_course(student_email=student['student_email'], course_name=course)


if __name__ == '__main__':
    add_courses()
    add_students()
    add_student_to_course()
    print(db.get_all_students_for_course('Python Pro'))
    print(db.get_student_with_courses('floreskerry@example.com'))
    db.update_student(email='michael05@example.com', first_name='Petro', last_name='Petrenko')
    db.delete_course(course_name='SMM')
    db.delete_student(email='michael05@example.com')
