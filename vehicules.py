class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0

    def start(self):
        self.started = True
        print(f"{self.make} {self.model} est démarrée.")

    def stop(self):
        self.started = False
        self.speed = 0
        print(f"{self.make} {self.model} est arrêtée.")

    def accelerate(self, value):
        if self.started:
            self.speed += value
            print(f"Vitesse actuelle : {self.speed} km/h")
        else:
            print("Car is not started!")

    def brake(self, value):
        if self.started:
            self.speed = max(0, self.speed - value)
            print(f"Braking to {self.speed} km/h...")
        else:
            print("Car is not started!")

# --- TEST COMPLET ---
ford_mustang = Car("Ford", "Mustang", 2022, "Black")

ford_mustang.start()           
ford_mustang.accelerate(100)    
ford_mustang.brake(50)          
ford_mustang.stop()            
ford_mustang.accelerate(100)    