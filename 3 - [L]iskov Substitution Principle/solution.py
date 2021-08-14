from abc import ABC, abstractmethod
"""
Liskov Substitution Principle (Princípio de substituição de Liskov)

Uma subclasse deve ser substituível pela sua super classe (ou classe base)
 sem quebrar o sistema.
"""


class Engine(ABC):
    pass


class Transport(ABC):
    name: str
    speed: float


class TransportWithoutEngines(Transport, ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class TransportWithEngines(Transport, ABC):
    engine: Engine

    @abstractmethod
    def start_engine(self) -> None:
        pass


"""
Agora as classes ficam mais especializadas, mantendo corretamente o LSP
"""


class Car(TransportWithEngines):
    def start_engine(self) -> None:
        pass


class Bicycle(TransportWithoutEngines):
    def move(self) -> None:
        pass
