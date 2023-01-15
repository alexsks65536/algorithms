class Person:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def health_up(self):
        self.health += 100


p = Person('Alex', 80)
print(p.name)
print(p.health)
p.health_up()
print(p.health)
p.health_up()
print(p.health)