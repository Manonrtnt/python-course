# modulo 26
# code ascii lettre de l'alphabet
# décallage de 1

def ceasar_cipher(text:str,offset:int) -> str:
    result = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            result+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            result += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            result += chr((ord(ch) + n-97) % 26 + 97)
    
    return result

plaintext = "HELLO EVERYONE"
n = 1
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + ceasar_cipher(plaintext,n))