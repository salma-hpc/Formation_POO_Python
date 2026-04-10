import json
import pickle

# On définit la classe de base
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# On définit le "Super-pouvoir" (le Mixin)
class SerializerMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

# On crée la classe finale en combinant les deux
class Employee(SerializerMixin, Person):
    def __init__(self, name, age, salary):
        # Initialise la partie Personne
        super().__init__(name, age)
        # Ajoute l'attribut spécifique à l'Employé
        self.salary = salary