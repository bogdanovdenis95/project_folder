class Vacancy:
    def __init__(self, title, link, salary, description):
        """
               Инициализирует объект Vacancy.

               Args:
                   title (str): Заголовок вакансии.
                   link (str): Ссылка на вакансию.
                   salary (str): Информация о зарплате.
                   description (str): Описание вакансии.

               Returns:
                   None
               """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        """
                Возвращает строковое представление объекта Vacancy.

                Returns:
                    str: Строковое представление объекта Vacancy.
                """
        return f"Vacancy(title='{self.title}', salary='{self.salary}')"
