# CLASSE PARENTE (Générique) 
class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        # On définit les caractéristiques de base de tout ce qui vole
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_specs(self):
        # Affiche les specs communes
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")

# CLASSE ENFANT (Spécialisée) 
class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        # super().__init__ appelle le constructeur de Aircraft.
        # Cela évite de réécrire self.thrust = thrust, etc.
        super().__init__(thrust, lift, max_speed)
        # On ajoute ensuite l'attribut spécifique à l'hélicoptère
        self.num_rotors = num_rotors

    def show_technical_specs(self):
        # STRATÉGIE D'EXTENSION :
        # 1. On appelle d'abord la méthode du parent pour afficher les 3 specs de base
        super().show_technical_specs()
        # 2. On ajoute notre propre ligne à la suite
        print(f"Number of rotors: {self.num_rotors}")