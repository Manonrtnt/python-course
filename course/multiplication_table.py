# L’utilisateur entre un nombre. Le programme stock
# les 10 premiers résultats de la table de
# multiplication choisie par l’utilisateur dans une
# liste puis affiche cette liste.

# BONUS
# Signaler au passage, à l’aide d’une astérisque,
# ceux qui sont des multiples de 3 

input = int(input('Quelle table voulez-vous afficher ? '))
multiplicationList =  []

for i in range(1,11):
    result = i*input
    if result % 3 == 0 :
        result3 = str(result) + "*"
        multiplicationList.append(result3)
    else :
        multiplicationList.append(result)

print(multiplicationList)