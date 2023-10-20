# Le programme tire un nombre aléatoire entre 0 et 100.
# Ensuite, la personne doit trouver le nombre en recevant
# comme indication si le nombre est trop grand ou trop
# petit.
# A la fin, le programme doit dire combien de coups ont
# été joués.

# importing the random module
import random

level = int(input('Enter level from 1 to 3 : '))

if level == 1 :
    randomLevel = 10
elif level == 2 :
    randomLevel = 100
elif level == 3 :
    randomLevel = 1000

print(f'you choose level {level} with randon number max {randomLevel}')

randomNumber = random.randint(0,randomLevel)
personNumber = 0

while personNumber != randomNumber : 
    print("Tapez un nombre entier :")
    personNumber = int(input())
    if personNumber > randomNumber :
            print("c'est moins\n")
    elif personNumber < randomNumber:
            print("c'est plus\n")
    else :
            print("c'est gagné")