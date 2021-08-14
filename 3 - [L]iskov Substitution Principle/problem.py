from abc import ABC, abstractmethod
"""
Liskov Substitution Principle (Princípio de substituição de Liskov)

Uma subclasse deve ser substituível pela sua super classe (ou classe base)
 sem quebrar o sistema.
"""

"""
Esse tipo de problema pode ocasionar com problema de abstração, feita incorretamente.

Exemplo clássico do "Se parece como um pato, grasna como um pato, mas precisa de bateria"
"""


class Engine(ABC):
    pass


class Transport(ABC):
    name: str
    speed: float
    engine: Engine

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Transport):
    def start_engine(self) -> None:
        pass

"""
Até aqui tudo bem, um carro é capaz de iniciar o motor
"""


class Bicycle(Transport):
    def start_engine(self) -> None:
        pass

"""
Bicicleta não tem motor, então a implementação fica vazia, podendo acarretar
num problema no sistema.
"""