from abc import ABC, abstractmethod
import json

class AbstractFileManager(ABC):
    @abstractmethod
    def save_vacancies(self, filename, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self, filename):
        pass

class JSONFileManager(AbstractFileManager):
    def save_vacancies(self, filename, vacancies):
        """
        Сохраняет список вакансий в файл в формате JSON.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            vacancies_data = []
            for vacancy in vacancies:
                vacancy_data = {
                    'id': vacancy['id'],
                    'name': vacancy['name'],
                    'salary': vacancy['salary'],
                    'description': vacancy['description'],
                    'company_name': vacancy['company_name']
                }
                vacancies_data.append(vacancy_data)
            json.dump(vacancies_data, file, indent=4)

    def load_vacancies(self, filename):
        """
        Загружает список вакансий из файла.
        """
        with open(filename, 'r') as file:
            vacancies = json.load(file)
        return vacancies

class DataManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def save_vacancies(self, filename, vacancies):
        """
        Сохраняет список вакансий в файл с использованием file_manager.
        """
        self.file_manager.save_vacancies(filename, vacancies)

    def load_vacancies(self, filename):
        """
        Загружает список вакансий из файла с использованием file_manager.
        """
        return self.file_manager.load_vacancies(filename)
