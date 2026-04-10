import json
import pickle

# Classe de base pour définir une personne
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# L'objet "SPÉCIALISTE" : il sait transformer n'importe quel objet en JSON ou Pickle
class Serializer:
    def __init__(self, instance):
        self.instance = instance

    def to_json(self):
        # Transforme les données de l'objet en format texte JSON
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        # Transforme les données de l'objet en format binaire Pickle
        return pickle.dumps(self.instance.__dict__)

# La classe principale
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    # LA MÉTHODE MAGIQUE : elle s'active si on appelle une méthode qui n'existe pas ici
    def __getattr__(self, attr):
        # 1. On crée un Serializer pour cet employé
        # 2. On lui délègue la recherche de la méthode (ex: .to_json())
        # C'est une redirection automatique !
        return getattr(Serializer(self), attr)