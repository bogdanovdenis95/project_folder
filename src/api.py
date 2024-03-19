from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        """
               Абстрактный метод для получения списка вакансий.

               Args:
                   search_text (str): Текст поискового запроса.

               Returns:
                   list: Список вакансий.
               """
        pass





class HeadHunterAPI(AbstractAPI):
    def get_vacancies(self, search_query):
        """
               Получает список вакансий с сайта HeadHunter по заданному поисковому запросу.

               Args:
                   search_query (str): Поисковый запрос.

               Returns:
                   list: Список вакансий.
               """
        pass
