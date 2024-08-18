# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager
# (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name=name, salary=salary, **kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language, **kwargs):
        super().__init__(name=name, salary=salary, **kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name=name, salary=salary, department=department, programming_language=programming_language)
        self.team_size = team_size

    def __str__(self):
        return (f"TeamLead {self.name}, Salary: {self.salary}, "
                f"Department: {self.department}, Programming Language: {self.programming_language}, "
                f"Team Size: {self.team_size}")


team_lead = TeamLead(name="Jack Dawson", salary=100, department="Titanic", programming_language="Python", team_size=1500)
print(team_lead)
