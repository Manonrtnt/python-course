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
