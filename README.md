# python-course

## Python fundamentals

### [main.py](/course/main.py)
Test virtual environment on vs code
> create : `py -m venv conv-venv`

> execute : `course-venv\script\activate`

```python
  first_name = 'Paul'
  print(first_name)
```
---
### [convert.py](/course/convert.py)
> Écrire un programme qui convertit en m/h une vitesse donnée en km/h.
> Rappel : 1 mile = 1,609 km

> Bonus : Arrondir le résultat au centième près

```python
  input = float(input('Veuillez entrer une vitesse en km/h : '))
  KMH_to_MPH = 1.609
  
  convert = input/KMH_to_MPH
  roundCounvert = round(convert, 2)
  
  print(f'your value in m/s is: {roundCounvert}')
  # other method round :.2F
  print(f'your value {input} km/h in m/s is: {convert:.2F}')
```
---
### [more_less.py](/course/more_less.py)
> Faire le jeu du plus ou moins
```python
  import random

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
```
> Bonnus : Faire un menu permettant de choisir une difficulté
```python
  level = int(input('Enter level from 1 to 3 : '))
  
  if level == 1 :
      randomLevel = 10
  elif level == 2 :
      randomLevel = 100
  elif level == 3 :
      randomLevel = 1000
```
---
## [unique_value.py](/course/unique_value.py)
> Écrire un programme qui créera une nouvelle liste en ne gardant que les valeurs uniques.
```python
  from collections import Counter

  number = [8, 7, 11, 7, 2, 10, 5, 8]

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
```
---
## [multiplication_table.py](/course/multiplication_table.py)
> L’utilisateur entre un nombre. Le programme stock
> les 10 premiers résultats de la table de
> multiplication choisie par l’utilisateur dans une
> liste puis affiche cette liste.

> BONUS : Signaler au passage, à l’aide d’une astérisque, ceux qui sont des multiples de 3 

```python
  input = int(input('Quelle table voulez-vous afficher ? '))
  multiplicationList =  []

  for i in range(1,10):
      result = i*input
      if result % 3 == 0 :
          result3 = str(result) + "*"
          multiplicationList.append(result3)
      else :
          multiplicationList.append(result)

  print(multiplicationList)
```
---
## [spellPhoneNumber.py](/course/spellPhoneNumber.py)
> Écrire un programme qui épellera un numéro de téléphone en toute lettre.
```python

```
---
