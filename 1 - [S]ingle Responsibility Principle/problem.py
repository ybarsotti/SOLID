"""
Single Responsibility Principle (Princípio da responsabilidade única)

'Uma classe deve ter apenas um motivo para mudar'
Uma classe deve ter apenas um trabalho, Se uma classe tem mais de uma
responsabilidade, vira acoplada. Uma mudança em uma responsabilidade
resulta na modificação de outra responsabilidade.
"""


"""
A classe Livro viola o SRP.

O problema da classe livro é que ela tem responsabilidade tanto de gerenciar
o banco de dados e o gerenciamento das propriedades do livro. 
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


    def save(self, book: Book) -> None:
        """Lógicas de salvamento, validação"""

