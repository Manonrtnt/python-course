# Écrire un programme qui créera une nouvelle liste
# en ne gardant que les valeurs uniques.

from collections import Counter

number = [8, 7, 11, 7, 2, 10, 5, 8]
result = []

# Traverse for all elements
def uniqueListAppend(list):
    if number not in result :
        result.append(number)
    
    print(result)


# Use collection
def uniqueWithCounter(list):
    #using * symbol
    print(*Counter(list))

print("the unique values from 1st list is")
uniqueListAppend(number)
uniqueWithCounter(number)