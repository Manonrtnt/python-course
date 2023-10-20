# Écrire un programme qui créera une nouvelle liste
# en ne gardant que les valeurs uniques.

from collections import Counter

number = [8, 7, 11, 7, 2, 10, 5, 8]

# Traverse for all elements
def uniqueListAppend(list):
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    print(unique_list)

# Use collection
def uniqueWithCounter(list):
    #using * symbol
    print(*Counter(list))

print("the unique values from 1st list is")
uniqueListAppend(number)
uniqueWithCounter(number)