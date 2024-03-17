import unittest
from vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def test_vacancy_creation(self):
        title = 'Python Developer'
        link = 'https://example.com'
        salary = '100000 RUR'
        description = 'Description of the vacancy'
        vacancy = Vacancy(title, link, salary, description)
        self.assertIsInstance(vacancy, Vacancy)
        self.assertEqual(vacancy.title, title)
        self.assertEqual(vacancy.link, link)
        self.assertEqual(vacancy.salary, salary)
        self.assertEqual(vacancy.description, description)

if __name__ == '__main__':
    unittest.main()
