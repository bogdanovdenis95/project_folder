import unittest
from unittest.mock import patch, MagicMock
from main import search_vacancies, save_vacancies, load_vacancies, user_interaction

class TestMain(unittest.TestCase):
    @patch('main.HeadHunterAPI')
    def test_search_vacancies(self, MockHeadHunterAPI):
        # Создаем экземпляр макета класса HeadHunterAPI
        mock_api_instance = MockHeadHunterAPI.return_value
        # Задаем поведение макета
        mock_api_instance.get_vacancies.return_value = [
            {"title": "Python Developer", "salary": "100000 RUR"},
            {"title": "Frontend Developer", "salary": "90000 RUR"}
        ]
        # Вызываем функцию, которую тестируем
        result = search_vacancies(mock_api_instance, "python")
        # Проверяем, что функция корректно обрабатывает полученные данные
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["title"], "Python Developer")
        self.assertEqual(result[1]["title"], "Frontend Developer")

    @patch('main.DataManager')
    def test_save_vacancies(self, MockDataManager):
        # Создаем экземпляр макета класса DataManager
        mock_data_manager_instance = MockDataManager.return_value
        # Вызываем функцию, которую тестируем
        save_vacancies(mock_data_manager_instance, "test_file.json", [{"title": "Python Developer", "salary": "100000 RUR"}])
        # Проверяем, что метод сохранения вакансий был вызван с правильными параметрами
        mock_data_manager_instance.save_vacancies.assert_called_once_with("test_file.json", [{"title": "Python Developer", "salary": "100000 RUR"}])

    @patch('main.DataManager')
    def test_load_vacancies(self, MockDataManager):
        # Создаем экземпляр макета класса DataManager
        mock_data_manager_instance = MockDataManager.return_value
        # Задаем поведение макета
        mock_data_manager_instance.load_vacancies.return_value = [{"title": "Python Developer", "salary": "100000 RUR"}]
        # Вызываем функцию, которую тестируем
        result = load_vacancies(mock_data_manager_instance, "test_file.json")
        # Проверяем, что функция корректно обрабатывает полученные данные
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Python Developer")

    @patch('builtins.input', side_effect=["python", "yes", "yes"])
    def test_user_interaction(self, mock_input):
        # Создаем макеты классов HeadHunterAPI и DataManager
        mock_api_instance = MagicMock()
        mock_data_manager_instance = MagicMock()
        # Задаем поведение макетов
        mock_api_instance.get_vacancies.return_value = [
            {"title": "Python Developer", "salary": "100000 RUR"}
        ]
        mock_data_manager_instance.load_vacancies.return_value = [
            {"title": "Python Developer", "salary": "100000 RUR"}
        ]
        # Вызываем функцию, которую тестируем
        with patch('main.HeadHunterAPI', return_value=mock_api_instance), \
             patch('main.DataManager', return_value=mock_data_manager_instance):
            user_interaction()
        # Проверяем, что функция взаимодействия с пользователем работает правильно
        mock_api_instance.get_vacancies.assert_called_once_with("python")
        mock_data_manager_instance.save_vacancies.assert_called_once()
        mock_data_manager_instance.load_vacancies.assert_called_once()

if __name__ == '__main__':
    unittest.main()
