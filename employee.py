from datetime import datetime

class Employee:
    # 1. Attribut de classe : Partagé par TOUS les employés
    company = "Example, Inc."

    # 2. Le Constructeur : On donne le nom et la date (en texte "YYYY-MM-DD")
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date # Ici, ça va appeler le @setter automatiquement

    # 3. La Property : Pour protéger et transformer la date
    @property 
    def birth_date(self):
        return self._birth_date # On lit la version "cachée" avec l'underscore
        

    @birth_date.setter
    def birth_date(self, value):
        # On transforme le texte reçu en un vrai objet de date Python
        self._birth_date = datetime.fromisoformat(value)

    # 4. Méthode Métier : Calcule l'âge en fonction d'aujourd'hui
    def compute_age(self):
        today = datetime.today()
        # Calcul de base sur l'année
        age = today.year - self.birth_date.year
        
        # On crée l'anniversaire de cette année pour vérifier s'il est déjà passé
        birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day
        )
        # Si aujourd'hui est avant l'anniversaire, on enlève 1 an
        if today < birthday:
            age -= 1
        return age

    # 5. Méthode de Classe : Pour créer un employé depuis un dictionnaire (JSON)
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict) # Les ** "déballent" le dictionnaire automatiquement

    # 6. Affichage Joli (print)
    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"

    # 7. Affichage Technique (débogage)
    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"name='{self.name}', "
            f"birth_date='{self.birth_date.strftime('%Y-%m-%d')}')"
        )        