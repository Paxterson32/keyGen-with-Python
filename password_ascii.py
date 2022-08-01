
from random import randint
import string

def select_random_letter(source_data):
    pos = randint(0,len(source_data)-1)
    return source_data[pos]


def find_password(size,source_data):
    sum = 0
    password=""
    while sum < size:
        letter = select_random_letter(source_data)
        temp = ord(letter)
        if (sum + temp) == size:
            password += letter
            return password
        elif (sum + temp ) > size:
            val = size - sum
            letter = chr(val)
            password += letter
            return password
        else :
            sum += temp
            password += letter

  

source = string.ascii_letters + string.digits

size_targeted = int(input("Entrez la valeur ascii recherchée : "))
count = int(input("Nombre de mdp recherché(s) : "))

for i in range(0, count):
    print(find_password(size_targeted,source))
