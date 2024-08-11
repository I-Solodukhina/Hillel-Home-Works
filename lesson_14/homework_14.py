# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, second_name, age, average_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_score = average_score

    def change_average_score(self, average_sc):
        self.average_score = average_sc
        return self.average_score

    def __str__(self):
        return f'Name: {self.first_name}\nSurname: {self.second_name}\nAge: {self.age}\nAverage: {self.average_score}'


student = Student('James', 'Cameron', 69, 11.0)
print(student)
student.change_average_score(15.0)
print(student)
