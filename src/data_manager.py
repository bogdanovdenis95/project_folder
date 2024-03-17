import json

class DataManager:
    def save_vacancies(self, filename, vacancies):
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
        with open(filename, 'r') as file:
            vacancies = json.load(file)
        return vacancies