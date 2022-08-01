
from random import randint
import string

# On va commencer par mettre tous les caractères utilisables dans une liste
source = string.ascii_letters + string.digits + string.punctuation

def createPassword(size,source):
    source_length = len(source) - 1
    password=""
    for i in range (0, size):
        pos = randint(0, source_length)
        password += source[pos]
    return password


pass_size = int(input("Taille du mot de passe à générer ? : "))
pass_number = int(input("Nombre de mot(s) de passe : "))

for i in range(0, pass_number):
    print(createPassword(pass_size,source))