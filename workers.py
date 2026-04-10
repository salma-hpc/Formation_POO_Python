#  CLASSE PARENTE 
class Worker:
    def __init__(self, name, address, hourly_salary):
        self.name = name
        self.address = address
        self.hourly_salary = hourly_salary

    def show_profile(self):
        print("== Worker profile ==")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Hourly salary: {self.hourly_salary}")

    def calculate_payroll(self, hours=40):
        # Calcul standard : salaire horaire simple
        return self.hourly_salary * hours

# SOUS-CLASSE AVEC REDÉFINITION 
class Manager(Worker):
    def __init__(self, name, address, hourly_salary, hourly_bonus):
        # On réutilise l'initialisation du parent pour les données de base
        super().__init__(name, address, hourly_salary)
        # On ajoute l'attribut spécifique au Manager
        self.hourly_bonus = hourly_bonus

    def calculate_payroll(self, hours=40):
        # REDÉFINITION TOTALE : 
        # Ici, on n'utilise pas super().calculate_payroll() car la formule change.
        # On remplace l'ancien calcul par le nouveau (salaire + bonus).
        return (self.hourly_salary + self.hourly_bonus) * hours