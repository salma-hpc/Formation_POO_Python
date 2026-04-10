# NIVEAU 1 : LA CLASSE DE BASE (Générique) 
class Animal:
    def __init__(self, name, sex, habitat):
        # Chaque animal, peu importe son espèce, a ces 3 caractéristiques
        self.name = name
        self.sex = sex
        self.habitat = habitat

# NIVEAU 2 : LES CLASSES INTERMÉDIAIRES (Familles) 
class Mammal(Animal):
    # Attribut de classe partagé par tous les mammifères
    unique_feature = "Mammary glands"

class Bird(Animal):
    unique_feature = "Feathers"

class Fish(Animal):
    unique_feature = "Gills"

#  NIVEAU 3 : LES SOUS-CLASSES DÉRIVÉES (Espèces) 
class Dog(Mammal):
    def walk(self):
        print(f"{self.name} the dog is walking on its 4 legs.")

class Penguin(Bird):
    # Note : Bien qu'il soit un oiseau, le pingouin ne vole pas, il nage !
    def swim(self):
        print(f"{self.name} the penguin is swimming in {self.habitat}.")

class Shark(Fish):
    def swim(self):
        print(f"{self.name} the shark is swimming silently.")