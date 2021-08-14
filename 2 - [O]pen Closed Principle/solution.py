from collections.abc import Iterable
from math import pi
from abc import ABC, abstractmethod

"""
Open Closed Principle (Princípio Aberto Fechado)

'Entidades devem ser abertas para extensão, mas fechado para modificação'
"""


"""
Uma forma de resolver o problema é criar uma classe base para os formatos 
"""


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """ Calcula a área de um formato """


"""
A partir daí todos os formatos implementarão os métodos da classe abstrata 
"""


class Rectangle(Shape):
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return self.radius * self.radius * pi


def area(shapes: Iterable[Shape]) -> float:
    area: float = 0
    for shape in shapes:
        area += shape.area()
    return area


"""
Agora nao precisamos nos preocupar com a implementação das formas
para novas formas, será necessário apenas herdar da classe Shape
"""

