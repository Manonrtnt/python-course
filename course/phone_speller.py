# Écrire un programme qui épellera un numéro de
# téléphone en toute lettre.

user_phone_number = input('Please enter a phone number : ')
result = ""

# Dictonnary
digits_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

for number in user_phone_number : 
    result += digits_mapping.get(number, '[Charact not mapped]') + ' '

# .strip remove useless space (start and end)
print(str(result.strip))