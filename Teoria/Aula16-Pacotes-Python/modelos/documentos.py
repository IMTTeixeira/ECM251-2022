from datetime import date


class Document:
    def __init__(self, authors = [], date = date.today()):
        self._authors = authors
        self._date = date
    def __str__(self):
        return f'Document: Authors:{self._authors} Date:{self._date}'
    def get_authors(self):
        return self._authors
    def get_date(self):
        return self._date
    def add_author(self, author):
        self._authors.append(author)

class Email(Document):
    def __init__(self, to, subject = "No subject", authors=[], date=date.today()):
        super().__init__(authors, date)
        self._to = to
        self._subject = subject
    def get_subject(self):
        return self._subject
    def get_to(self):
        return self._to
    def __str__(self):
        return f'Email: To:{self._to} Subject:{self._subject}  Authors{super().get_authors()} Date:{super().get_date()}'

class Book(Document):
    def __init__(self, title, authors = [], date = date.today()):
        super().__init__(authors, date)
        self._title = title
    def get_title(self):
        return self._title
    def __str__(self):
        return f'Book: Title:{self._title} - {super().__str__()}'