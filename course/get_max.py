# Définition de la fonction get_max
# A vous de l'implémenter :)

def get_max(numbers:list[float]) -> float:
    result = number[0]
    for number in numbers :
        if number > result : 
            result = number
    print(result)

numbersTest = [1,10,35,100,3]

get_max(numbersTest)