import os
from peewee import (
    Model,
    CharField,
    ForeignKeyField,
    PostgresqlDatabase
)


def is_running_in_docker():
    path_to_dockerenv = '/.dockerenv'
    return os.path.exists(path_to_dockerenv)


db = PostgresqlDatabase(
    database=os.getenv('POSTGRES_DB', 'solodushka_db'),
    user=os.getenv('POSTGRES_USER', 'solodushka'),
    password=os.getenv('POSTGRES_PASSWORD', '000000'),
    host='db' if is_running_in_docker() else '127.0.0.1',
    port=int(os.getenv('POSTGRES_PORT', 5432))
)


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


try:
    db.connect()
    db.create_tables([Students, Course, CourseStudents])
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    db.close()
