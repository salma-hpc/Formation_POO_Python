import math

# 1. Le descrepteur : C'est un contrôleur de données réutilisable
class PositiveNumber:
    # Cette méthode automatique récupère le nom de la variable (ex: "radius" ou "side")
    def __set_name__(self, owner, name):
        self._name = name

    # Cette méthode est appelée quand on veut LIRE la valeur (le Getter)
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    # Cette méthode est appelée quand on veut modifier la valeur (le Setter)
    def __set__(self, instance, value):
        # On centralise la validation ici pour toutes les classes
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        # Si c'est bon, on enregistre dans le dictionnaire de l'objet
        instance.__dict__[self._name] = value

# 2. La classe Circle utilise l'outil PositiveNumber
class Circle:
    radius = PositiveNumber()  # On branche le contrôleur sur 'radius'

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

# 3. La classe Square utilise aussi l'outil PositiveNumber
class Square:
    side = PositiveNumber()    # On branche le même contrôleur sur 'side'

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2