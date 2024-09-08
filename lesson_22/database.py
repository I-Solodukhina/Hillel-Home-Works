from peewee import (
    Model,
    CharField,
    ForeignKeyField,
    PostgresqlDatabase
)

# Параметри підключення до бази даних
db = PostgresqlDatabase(
    'solodushka_db',
    user='solodushka',
    password='000000',
    host='127.0.0.1',
    port=5432
)


# Визначення моделі таблиці
class Students(Model):
    email = CharField(default=None, primary_key=True)
    first_name = CharField(default=None)
    last_name = CharField(default=None)

    class Meta:
        database = db


class Course(Model):
    course_name = CharField(default=None, primary_key=True)

    class Meta:
        database = db


class CourseStudents(Model):
    student = ForeignKeyField(Students, backref='courses', field='email', on_delete='CASCADE')
    course = ForeignKeyField(Course, backref='students', field='course_name', on_delete='CASCADE')

    class Meta:
        database = db


db.connect()
db.create_tables([Students, Course, CourseStudents])
db.close()
