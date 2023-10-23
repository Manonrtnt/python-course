# un attribut statique est une variable associée à la classe
class Robot:
    # Attribut statique
    # Compter le nombre d'instanciation
    count = 0

    def __init__(self, name:str, actions:list[str]):
        self.name = name
        self.actions = actions
        Robot.count += 1
    
    # Méthode statique
    # Retourne le nom de la classe
    @staticmethod
    def get_class_name():
        return 'Robot'

# Première instanciation
r2d2 = Robot('R2D2', ['Move', 'Take'])
print(Robot.count)

# Seconde instanciation
wall_e = Robot('Walll-E', ['Climb', 'Wash'])
print(Robot.count)

print(Robot.get_class_name()) # Robot