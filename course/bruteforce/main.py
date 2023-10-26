import random
import string

## GENERATEUR MOT DE PASSE ##
# Écrire une fonction permettant de générer un mot de passe dont le nombre 
# de caractères est paramétrable.
# Caractères possibles : Majuscules / Minuscules / Chiffres / ( ) [ ] : ; ! 

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + "()[]:;!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Générer un mot de passe de 8 caractères
generate_password = generate_password(4)
print("Mot de passe généré :", generate_password)


# Check produit cartésien entre deux caractères. 
def brute_force_password(target_password: str) -> str:
    characters = string.ascii_letters + string.digits + "()[]:;!"
    password_length = 1

    while password_length <= 4:
        for char1 in characters:
            if password_length == 1:
                test_password = char1
                if test_password == target_password:
                    return test_password
            else:
                for char2 in characters:
                    if password_length == 2:
                        test_password = char1 + char2
                        if test_password == target_password:
                            return test_password
                    else:
                        for char3 in characters:
                            if password_length == 3:
                                test_password = char1 + char2 + char3
                                if test_password == target_password:
                                    return test_password
                            else:
                                for char4 in characters:
                                    test_password = char1 + char2 + char3 + char4
                                    if test_password == target_password:
                                        return test_password
        password_length += 1

    return None

# Exemple d'utilisation pour brute-force un mot de passe
found_password = brute_force_password(generate_password)
if found_password:
    print("Mot de passe trouvé:", found_password)
else:
    print("Mot de passe non trouvé.")


# Benchmark le temps de bruteforce nécessaire 
# cf cours. 

##Calcul des Combinatoires Possibles##

# Le nombre de combinaisons possibles pour un mot de passe de 4 caractères 
# avec les caractères possibles (majuscules, minuscules, chiffres, symboles) 
# est calculé comme suit :

# Le nombre de caractères possibles est la somme du nombre de majuscules (26), 
# de minuscules (26), de chiffres (10), et de symboles (7) pour un total de 69 
# caractères possibles.

# Pour un mot de passe de 4 caractères, 
# il y a 69 possibilités pour le premier caractère, 
# 69 pour le deuxième caractère, 
# 69 pour le troisième caractère, et 69 pour le quatrième caractère.

# Le nombre total de combinaisons possibles est donc calculé comme 69 * 69 * 69 * 69, 
# ce qui est égal à 17850681.

# Ainsi, il y a 17 850 681 combinaisons possibles pour un mot de passe 
# de 4 caractères avec les caractères spécifiés.