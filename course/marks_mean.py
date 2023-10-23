# Écrire un programme qui demande en continue à
# l’utilisateur d’entrer des notes d’élèves. La boucle se
# termine seulement si l’utilisateur entre une valeur
# négative. Lorsque cela arrive, afficher le nombre de notes
# entrées, et calculer la moyenne de toutes les notes.
# Si l’utilisateur entre autre chose qu’un nombre, l’erreur
# doit être traitée.
# Si l’utilisateur ne rentre aucune note et quitte le
# programme immédiatement, l’erreur doit également être
# traitée.

# count = 0
# inputUser = int(input('Entrer un nombre positif : '))
# result = 0
# count = 0

# # Acquisition des notes
# while inputUser >= 0 :
#     inputUser = input('Entrer un nombre positif : ')
#     count +=1
#     try :
#         inputUser = int(inputUser)
#         result += inputUser
#     except ValueError :
#         ("Vous n'avez pas entre de nombre")
#         break

# try : 
#     result = result / count
#     print(f'La moyenne des {count} notes est de : {result}')
# except ZeroDivisionError : 
#     print(f'Il y a : {count} note(s)')
#     print("L'utilisateur n'a pas saisi de note")

## CORRECTION ##
# Acquisition des notes
marks = []

while True:
    mark = input('Veuillez entrer un nombre positif :')
    try:
        mark = int(mark)

    except ValueError:
        print('Vous n\'avez pas entrer un nombre')
    else:
        if (mark > 0):
            marks.append(mark)
        else:
            break

# Calcul de la moyenne
try:
    average = sum(marks) / len(marks)
except ZeroDivisionError:
    print('Vous n\'avez rentré aucune note')
else:
    print(f'La moyenne est {average:.2f}')