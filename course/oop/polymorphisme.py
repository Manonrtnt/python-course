# Diférent comportement pour une même méthode
class Animal():
    def move():
        pass

class Eagle(Animal):
    def move(self) -> None:
        print('Eagle is flying')

class Dolphin(Animal):
    def move(self) -> None:
        print('Dolphin is swimming')
        
class Dog(Animal):
    def move(self) -> None:
        print('Dog is running')

animals = [Eagle(), Dolphin(), Dog()]

for animal in animals:
    animal.move()
