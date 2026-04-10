from abc import ABC, abstractmethod
import math

# La classe ABC : c'est le "contrat" ou le modèle obligatoire
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        # Cette méthode DOIT être définie dans les classes enfants
        pass

    @abstractmethod
    def get_perimeter(self):
        # Cette méthode DOIT aussi être définie obligatoirement
        pass

# Première classe concrète : le Cercle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
