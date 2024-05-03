# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack(self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form

# # Створення об'єкта Pikachu
# pikachu = Pokemon("Pikachu", "Electric", 100)

# # Використання методів
# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")




class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
print(p._Person__is_admin)
