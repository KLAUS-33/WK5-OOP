# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, and I protect {self.city} with my {self.power}!"

# Subclass showing inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, altitude):
        super().__init__(name, power, city)
        self.altitude = altitude

    def fly(self):
        return f"{self.name} is flying at {self.altitude} feet above {self.city}!"

# Create objects
hero1 = Superhero("NightShadow", "invisibility", "Nairobi")
hero2 = FlyingSuperhero("SkyBlazer", "flight", "Mombasa", 10000)

print(hero1.introduce())
print(hero2.introduce())
print(hero2.fly())
