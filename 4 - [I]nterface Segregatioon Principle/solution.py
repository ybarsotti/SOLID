from abc import ABC, abstractmethod

"""
Interface Segregation Principle (Princípio da Segregação de Interface)

Muitas interfaces específicas são melhores que uma interface de propósito geral,
um cliente(classes e/ou algoritmos) não deve ser forçado a depender de métodos
que não utilizarão.
"""

"""
Uma forma de resolver e respeitar a premissa é gerando interfaces (nesse caso
classes abstratas) específicas para suas classes
"""


class IMobileTelephone(ABC):
    @abstractmethod
    def ring(self) -> None:
        pass

    @abstractmethod
    def dial(self) -> None:
        pass

    @abstractmethod
    def take_photo(self) -> None:
        pass

    @abstractmethod
    def connect_internet(self) -> None:
        pass


class ICommonPhone(ABC):
    @abstractmethod
    def ring(self) -> None:
        pass

    @abstractmethod
    def dial(self) -> None:
        pass

"""
Agora todas as classes implementação os métodos das superclasses
"""


class MobilePhone(IMobileTelephone):
    def ring(self) -> None:
        pass

    def dial(self) -> None:
        pass

    def take_photo(self) -> None:
        pass

    def connect_internet(self) -> None:
        pass


class CommonPhone(ICommonPhone):
    def ring(self) -> None:
        pass

    def dial(self) -> None:
        pass

