from abc import ABC, abstractmethod

"""
Interface Segregation Principle (Princípio da Segregação de Interface)

Muitas interfaces específicas são melhores que uma interface de propósito geral,
um cliente(classes e/ou algoritmos) não deve ser forçado a depender de métodos
que não utilizarão.
"""

"""
Um exemplo bem comum é uma interface genérica (nesse caso uma classe abstrata)
e algumas classes não farão uso de todos os métodos herdados
"""


class Telephone(ABC):
    @abstractmethod
    def ring(self) -> None:
        pass

    @abstractmethod
    def dial(self) -> None:
        pass

    @abstractmethod
    def take_photo(self) -> None:
        pass


class MobilePhone(Telephone):
    def ring(self) -> None:
        """Implementação do toque"""

    def dial(self) -> None:
        """Implementação de discagem"""

    def take_photo(self) -> None:
        """Implementação de tirar foto"""


class CommonPhone(Telephone):
    def ring(self) -> None:
        """Implementação do toque"""

    def dial(self) -> None:
        """Implementação de discagem"""

    def take_photo(self) -> None:
        raise NotImplementedError

"""
Notamos que a classe CommonPhone não utilizará o método take_photo
que foi obrigado a implementar, retornando um erro
"""