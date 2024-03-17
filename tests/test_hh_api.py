import unittest
from hh_api import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    def test_get_vacancies(self):
        search_query = 'python'
        vacancies = self.api.get_vacancies(search_query)
        # Проверяем, что список вакансий не пустой
        self.assertTrue(vacancies)
        # Проверяем, что каждая вакансия содержит необходимые поля
        for vacancy in vacancies:
            self.assertIn('id', vacancy)
            self.assertIn('name', vacancy)
            self.assertIn('salary', vacancy)
            self.assertIn('description', vacancy)
            self.assertIn('company_name', vacancy)

if __name__ == '__main__':
    unittest.main()
