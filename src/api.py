from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_text):
        pass



class HeadHunterAPI(AbstractAPI):
    def get_vacancies(self, search_query):

        pass
