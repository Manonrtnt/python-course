# Faire une analyse statistique d'un texte, celle-ci affichera un
# dictionnaire avec le décompte de chaque lettre.
import string

text = "Hello World !"
# alphabet = dict.fromkeys(string.ascii_lowercase, 0)
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = {}
print(alphabet)

for char in alphabet :
    result[char] = text.count(char)

print(result)