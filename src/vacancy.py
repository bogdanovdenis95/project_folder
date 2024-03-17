class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f"Vacancy(title='{self.title}', salary='{self.salary}')"
