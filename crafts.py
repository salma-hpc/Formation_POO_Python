#  CLASSE DE BASE (Le "Grand-Parent") 
# Cette classe contient ce qui est commun à TOUS les véhicules
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Moteur allumé !")

    def stop(self):
        # On ajoute cette méthode pour corriger l'erreur précédente
        print("Moteur arrêté.")

    def show_technical_specs(self):
        # On affiche chaque info sur une nouvelle ligne pour la lisibilité
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")

#  CLASSES PARENTES (Les "Spécialisations") 
# Car hérite de Vehicle : elle "est un" véhicule
class Car(Vehicle):
    def drive(self):
        print("La voiture roule sur la route...")

# Aircraft hérite aussi de Vehicle
class Aircraft(Vehicle):
    def fly(self):
        print("L'avion vole dans le ciel...")

#  CLASSE HYBRIDE (L'enfant avec l'Héritage Multiple) 
# FlyingCar hérite de Car ET de Aircraft en même temps.
# Elle récupère TOUTES les méthodes de ses parents et de son grand-parent.
class FlyingCar(Car, Aircraft):
    # On utilise 'pass' car on n'a rien besoin d'ajouter, 
    # le mélange des parents suffit à créer l'objet.
    pass