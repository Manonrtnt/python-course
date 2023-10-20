# Écrire un programme qui convertit en m/h une vitesse donnée en km/h.
# Rappel : 1 mile = 1,609 km
# Bonus : Arrondir le résultat au centième près.

input = float(input('Veuillez entrer une vitesse en km/h : '))
KMH_to_MPH = 1.609

convert = input/KMH_to_MPH
roundCounvert = round(convert, 2)

print(f'your value in m/s is: {roundCounvert}')
# other method round :.2F
print(f'your value {input} km/h in m/s is: {convert:.2F}')
