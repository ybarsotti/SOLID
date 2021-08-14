from collections.abc import Iterable
from math import pi

"""
Open Closed Principle (Princípio Aberto Fechado)

'Entidades devem ser abertas para extensão, mas fechado para modificação'
"""


class Rectangle:
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


"""
A classe AreaCalculator funciona bem para calcular a área de um quadrado 
"""


class AreaCalculator:
    @staticmethod
    def area(shapes: Iterable[Rectangle]) -> float:
        area: float = 0

        for shape in shapes:
            area += shape.width * shape.height

        return area


"""
Porém, se precisarmos calcular a área de um círculo teríamos que checar
o tipo de cada objeto para poder calcular corretamente a área por objeto.
"""


class Circle:
    radius: float

    def __init__(self, radius: float):
        self.radius = radius


class AreaCalculator:
    @staticmethod
    def area(shapes: Iterable[object]) -> float:
        area: float = 0

        for shape in shapes:
            if isinstance(shape, Rectangle):
                area += shape.width * shape.height
            elif isinstance(shape, Circle):
                area += shape.radius * shape.radius * pi

        return area

"""
O que acaba fazendo com que tenhamos que aumentar a quantidade de IFs 
para cada objeto a ser calculado, a longo prazo pode virar um código dificil
de dar manutenção e com o risco de acabar quebrando alguma funcionalidade.
"""