"""
Single Responsibility Principle (Princípio da responsabilidade única)

'Uma classe deve ter apenas um motivo para mudar'
Uma classe deve ter apenas um trabalho, Se uma classe tem mais de uma
responsabilidade, vira acoplada. Uma mudança em uma responsabilidade
resulta na modificação de outra responsabilidade.
"""


"""
Uma forma de resolver o problema é desacoplar as responsabilidades em diferentes
classes, e essa classe tem apenas a responsabilidade de armazenar o registro no banco.
"""


class Book:
    _author: str
    _title: str

    def __init__(self, author: str, title: str):
        self._author = author
        self._title = title

    def get_author(self) -> str:
        return self._author

    def get_title(self) -> str:
        return self._title


class BookDB:
    def get_book(self, id: int) -> Book:
        pass

    def save(self, book: Book) -> Book:
        pass