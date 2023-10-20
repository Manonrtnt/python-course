# python-course

## Python fundamentals

### main.py
Test virtual environment on vs code
> create : `py -m venv conv-venv`

> execute : `course-venv\script\activate`

```python
  first_name = 'Paul'
  print(first_name)
```
---
### convert.py
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
### more_less.py
> Écrire un programme qui créera une nouvelle liste en ne gardant que les valeurs uniques.
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
