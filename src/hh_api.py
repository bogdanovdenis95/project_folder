import requests
from .api import AbstractAPI
from .vacancy import Vacancy

class HeadHunterAPI(AbstractAPI):
    def __init__(self, base_url='https://api.hh.ru'):
        self.base_url = base_url

    def get_vacancies(self, search_query):
        vacancies = []
        response = requests.get("https://api.hh.ru/vacancies", params={"text": search_query})
        response.raise_for_status()
        vacancies_data = response.json().get("items", [])
        for vacancy_data in vacancies_data:
            vacancy_id = vacancy_data.get('id')
            name = vacancy_data.get('name')
            salary = vacancy_data.get('salary', {})
            if salary:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                salary_currency = salary.get('currency')
                if salary_from is not None and salary_to is not None:
                    salary_info = f"{salary_from} - {salary_to} {salary_currency}"
                elif salary_from is not None:
                    salary_info = f"от {salary_from} {salary_currency}"
                elif salary_to is not None:
                    salary_info = f"до {salary_to} {salary_currency}"
                else:
                    salary_info = "Зарплата не указана"
            else:
                salary_info = "Зарплата не указана"
            description = vacancy_data.get('description', 'Описание отсутствует')
            company_name = vacancy_data.get('employer', {}).get('name', 'Название компании не указано')
            vacancies.append({"id": vacancy_id, "name": name, "salary": salary_info,
                              "description": description, "company_name": company_name})
        return vacancies
