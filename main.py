import requests
from src.hh_api import HeadHunterAPI
from src.data_manager import DataManager, JSONFileManager
from src.vacancy import Vacancy

def search_vacancies(api, search_query):
    """
        Поиск вакансий с использованием API.

        Args:
            api (HeadHunterAPI): Объект API для получения вакансий.
            search_query (str): Запрос для поиска вакансий.

        Returns:
            list: Список найденных вакансий.
        """
    try:
        vacancies = api.get_vacancies(search_query)
        print("Vacancies found:")
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"{index}. {vacancy}")
        return vacancies
    except requests.exceptions.HTTPError as e:
        print(f"Error occurred while fetching vacancies: {e}")


def save_vacancies(data_manager, filename, vacancies):
    """
        Сохранение списка вакансий в файл.

        Args:
            data_manager (DataManager): Менеджер данных для сохранения.
            filename (str): Имя файла для сохранения.
            vacancies (list): Список вакансий для сохранения.

        Returns:
            None
        """
    data_manager.save_vacancies(filename, vacancies)
    print(f"Vacancies saved to {filename}")


def load_vacancies(data_manager, filename):
    """
        Загрузка списка вакансий из файла.

        Args:
            data_manager (DataManager): Менеджер данных для загрузки.
            filename (str): Имя файла для загрузки.

        Returns:
            list: Список загруженных вакансий.
        """
    vacancies = data_manager.load_vacancies(filename)
    if vacancies:
        print("Vacancies loaded successfully:")
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"{index}. {vacancy}")
    else:
        print(f"No vacancies found in {filename}")
    return vacancies


def user_interaction():
    api = HeadHunterAPI()
    file_manager = JSONFileManager()  # Создаем объект JSONFileManager
    data_manager = DataManager(file_manager)  # Передаем его в конструктор DataManager
    filename = 'vacancies.json'

    search_query = input("Enter your search query: ")
    vacancies = search_vacancies(api, search_query)

    if vacancies:
        save_option = input("Do you want to save the found vacancies? (yes/no): ")
        if save_option.lower() == 'yes':
            save_vacancies(data_manager, filename, vacancies)

    load_option = input("Do you want to load vacancies from file? (yes/no): ")
    if load_option.lower() == 'yes':
        loaded_vacancies = load_vacancies(data_manager, filename)


if __name__ == "__main__":
    user_interaction()
