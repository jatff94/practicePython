import string
import random

def returnRandom(key):
    if key == 0:
        returnVal = random.choice(list_upper)
    elif key == 1:
        returnVal = random.choice(list_lower)
    elif key == 2:
        returnVal = random.choice(list_digits)
    else:
        returnVal = random.choice(list_symbols)

    return returnVal
        

list_upper = list(string.ascii_uppercase)
key_upper = 0

list_lower = list(string.ascii_lowercase)
key_lower = 1

list_digits = list(string.digits)
key_digits = 2

list_symbols= list(string.punctuation)
key_symbols = 3

password = list()

for x in range(0,10):
    key = random.randint(0,5)
    password.append(returnRandom(key))

print("".join(password))
