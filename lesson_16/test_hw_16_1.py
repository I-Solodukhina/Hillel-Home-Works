import unittest
from lesson_16.homework_16_1 import TeamLead


class TestTeamLead(unittest.TestCase):
    def setUp(self):
        self.team_lead = TeamLead(name="Alice", salary=120000, department="IT", programming_language="Python",
                                  team_size=10)

    def test_attributes(self):
        # Перевірка атрибутів з класу Manager
        self.assertTrue(hasattr(self.team_lead, 'department'))
        self.assertEqual(self.team_lead.department, "IT")

        # Перевірка атрибутів з класу Developer
        self.assertTrue(hasattr(self.team_lead, 'programming_language'))
        self.assertEqual(self.team_lead.programming_language, "Python")

        # Перевірка атрибутів з класу Employee
        self.assertTrue(hasattr(self.team_lead, 'name'))
        self.assertEqual(self.team_lead.name, "Alice")
        self.assertTrue(hasattr(self.team_lead, 'salary'))
        self.assertEqual(self.team_lead.salary, 120000)

        # Перевірка атрибуту team_size з класу TeamLead
        self.assertTrue(hasattr(self.team_lead, 'team_size'))
        self.assertEqual(self.team_lead.team_size, 10)


if __name__ == '__main__':
    unittest.main()
