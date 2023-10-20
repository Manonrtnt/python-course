# Le programme tire un nombre aléatoire entre 0 et 100.
# Ensuite, la personne doit trouver le nombre en recevant
# comme indication si le nombre est trop grand ou trop
# petit.
# A la fin, le programme doit dire combien de coups ont
# été joués.

# importing the random module
from random import randint

level = int(input('Enter level from 1 to 3 : '))

if level == 1 :
    random_level = 10
elif level == 2 :
    random_level = 100
elif level == 3 :
    random_level = 1000

print(f'you choose level {level} with randon number max {random_level}')

random_number = randint(0,random_level)
person_number = 0
attempts = 1

while person_number != random_number : 
    print("Tapez un nombre entier : ")
    person_number = int(input())
    attempts += 1
    if person_number > random_number :
        print("c'est moins\n")
    elif person_number < random_number:
        print("c'est plus\n")
    else :
        print(f"c'est gagné avec {attempts} essai(s)")