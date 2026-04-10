import math

class Circle:
    def __init__(self, radius):
        # L'affectation passe par le setter pour valider la donnée dès le début
        self.radius = radius

    @property
    def radius(self):
        """Le Getter : permet de lire la valeur."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Le Setter : permet de valider la valeur avant de l'enregistrer."""
        # On vérifie si c'est un nombre et s'il est positif
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def calculate_area(self):
        return math.pi * self._radius**2