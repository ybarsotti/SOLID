"""
Dependency Inversion Principle (Princípio da inversão de dependência)

Abstrações não devem depender de detalhes. Detalhes devem depender de abstração.
Módulos de alto nível não devem depender de módulos baixo nivel. Ambos devem
depender de abstrações.
"""


class XMLHttpRequestService:
    pass


class XMLHttpService(XMLHttpRequestService):
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url: str, options: dict):
        return self.xml_http_service.request(url, 'GET', options)

    def post(self, url: str, options: dict):
        return self.xml_http_service.request(url, 'POST', options)


"""
Nesse exemplo, Http é um componente alto nivel e XMLHttpService é o componente
baixo nivel. Violando o DIP.
"""
