from abc import ABC, abstractmethod

"""
Dependency Inversion Principle (Princípio da inversão de dependência)

Abstrações não devem depender de detalhes. Detalhes devem depender de abstração.
Módulos de alto nível não devem depender de módulos baixo nivel. Ambos devem
depender de abstrações.
"""

"""
A classe Http não deve se preocupar com o tipo do serviço utilizado, com isso
a gente abstrai para uma interface de conexão.
"""


class Connection(ABC):
    @abstractmethod
    def request(self, url: str, options: dict) -> None:
        pass


"""
A classe abstrata possui o método request. Então passamos como um argumento
para a classe Http
"""


class Http:
    """
    Agora a única dependência não é uma classe concreta, e sim uma abstração,
    se quisermos gerar uma instância da class Http, precisaremos apenas passar
    alguma classe que herde da classe (ou interface) Connection
    """
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        return self.http_connection.request(url, 'GET')

    def post(self, url: str, options: dict):
        return self.http_connection.request(url, 'POST')


class XMLHttpRequest:
    def open(self):
        pass

    def send(self):
        pass


class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()


"""
Agora podemos ter diversos Http connection e passá-los para a classe Http
sem causar erros.
"""


class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass
