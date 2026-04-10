import math 

# On définit la Classe
class Circle:
    
    # Le constructeur : c'est ici qu'on définit ce qu'un cercle doit avoir
    # 'self' représente l'objet lui-même qui sera créé
    def __init__(self, radius):
        # On enregistre le rayon à l'intérieur de l'objet
        self.radius = radius

    # Une méthode : c'est une action ou un calcul que l'objet peut faire
    def calculate_area(self):
        
        return math.pi * (self.radius ** 2)


ed = 200** 2