import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.filename = 'test_vacancies.json'

    def test_save_and_load_vacancies(self):
        vacancies = [
            {'id': '123', 'name': 'Python Developer', 'salary': '100000 RUR', 'description': 'Description', 'company_name': 'Company A'},
            {'id': '456', 'name': 'Web Developer', 'salary': '80000 RUR', 'description': 'Description', 'company_name': 'Company B'}
        ]
        # Сохраняем вакансии
        self.data_manager.save_vacancies(self.filename, vacancies)
        # Проверяем, что файл создан
        with open(self.filename, 'r') as file:
            self.assertTrue(file.read())
        # Загружаем вакансии из файла
        loaded_vacancies = self.data_manager.load_vacancies(self.filename)
        # Проверяем, что загруженные вакансии совпадают с сохраненными
        self.assertEqual(loaded_vacancies, vacancies)

    def tearDown(self):
        # Удаляем временный файл после выполнения тестов
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()
