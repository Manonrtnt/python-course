first_name = 'Paul'
print(first_name)

user = {
    "last_name": "Doe",
    "first_name": "John",
    "age": 20
}
# Retourne la liste des clefs du dictionnaire
list(user)
# Retourne un objet dict_keys
# (Liste) des clefs du dictionnaire
print(user.keys())
# dict_keys(['last_name', 'first_name', 'age'])

# Retourne un objet dict_values
# (Liste) des valeurs du dictionnaire
print(user.values())
# dict_values(['Doe', 'John', 20])

# Retourne un objet dict_items
# (Liste) de tuples (clef, valeur) du dictionnaire
print(user.items())
# dict_items([('last_name', 'Doe'), ('first_name', 'John'), ('age', 20)])


f = open('course\data\poem.txt')
poem = f.read()
# Debug plus facilement
print(type(f))
f.close()
print(poem)

try : 
    with open('./data/poem.txt') as f:
        poem = f.read()
        print(poem)
except FileNotFoundError : 
    print('Fichier non trouvé')

# Ecrire dans fichier txt.
oceans = [
    "Pacific",
    "Atlantic",
    "Indian",
    "Southern",
    "Arctic"
]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
    # Autre possibilité
    # print(ocean, file=f)

# a pour append 
oceans = [
    "Southern",
    "Arctic"
]
with open("oceans.txt", "a") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
    # Autre possibilité
    # print(ocean, file=f)

