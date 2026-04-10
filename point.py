from dataclasses import dataclass

# 1. Le décorateur @dataclass
# Il génère automatiquement le __init__, le __repr__ et le __eq__ (comparaison).
# Ona plus besoin d'écrire "self.x = x" !

@dataclass
class ThreeDPoint:
    # 2.
    # On précise que x, y et z peuvent être des entiers (int) OU des décimaux (float).
    x: int | float
    y: int | float
    z: int | float

    # 3. Méthode de classe (@classmethod)
    # 'cls' représente la classe elle-même. 
    @classmethod
    def from_sequence(cls, sequence):
        # L'étoile (*) "déballe" la liste pour donner les 3 arguments au constructeur.
        return cls(*sequence)

    # 4. Méthode statique (@staticmethod)
    # Elle ne dépend ni de l'objet (self) ni de la classe (cls).
    # C'est juste une fonction utilitaire rangée dans la classe par logique.
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")