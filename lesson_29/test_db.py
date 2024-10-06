import pytest
from unittest.mock import patch
from database_manager import DatabaseManager, Students, Course

@pytest.fixture
def db_manager():
    return DatabaseManager()

@patch('database_manager.db.close')
@patch('database_manager.db.connect')
@patch('database_manager.db.is_closed')
def test_connect_and_close(mock_is_closed, mock_connect, mock_close, db_manager):
    mock_is_closed.return_value = True

    db_manager.connect()
    mock_connect.assert_called_once()
    
    mock_is_closed.return_value = False
    
    db_manager.close()
    mock_close.assert_called_once()
    
    mock_is_closed.assert_called()


@patch('database_manager.Students.create')
def test_add_student(mock_create, db_manager):
    student_data = {
        'email': 'teststudent@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    }
    db_manager.add_student(**student_data)
    mock_create.assert_called_once_with(**student_data)
    
    
@patch('database_manager.Course.create')
def test_add_course(mock_create, db_manager):
    course_data = {
        'course_name': 'Python Pro'
    }
    db_manager.add_course(**course_data)
    mock_create.assert_called_once_with(**course_data)


@patch('database_manager.Students.select')
def test_get_all_students(mock_select, db_manager):
    mock_select.return_value = []
    students = db_manager.get_all_students()
    assert isinstance(students, list)


@patch('database_manager.Students.update')
def test_update_student(mock_update, db_manager):
    student_data = {
        'email': 'teststudent@example.com',
        'first_name': 'Jane',
        'last_name': 'Smith'
    }
    db_manager.update_student(**student_data)
    mock_update.assert_called_once_with(**student_data)


@patch('database_manager.Students.delete')
def test_delete_student(mock_delete, db_manager):
    email = 'teststudent@example.com'
    mock_delete.return_value = mock_delete
    db_manager.delete_student(email)
    mock_delete.assert_called_once()
    mock_delete().where.assert_called_once_with(Students.email == email)


@patch('database_manager.Course.delete')
def test_delete_course(mock_delete, db_manager):
    course_name = 'Python Pro'
    mock_delete.return_value = mock_delete
    db_manager.delete_course(course_name)
    mock_delete.assert_called_once()
    mock_delete().where.assert_called_once_with(Course.course_name == course_name)
