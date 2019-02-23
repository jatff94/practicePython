import random

def cows_and_bulls(comp_guess, user_guess):
    cow_bull = [0,0]

    for i in len(range(user_guess)):
        if user_guess[i] == comp_guess[i]:
            cow_bull[0] =+1
        else:
            cow_bull[1] =+1

    return cow_bull
    


#generate a random 4 digit number
random_guess = str(random.randint(1000,9999))

#user input
use_in = input("Enter your guess or quit: ")



while True:
    if use_in == 
