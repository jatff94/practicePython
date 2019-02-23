import random

rand_num = random.randint(1,9)
user_guess = int(input("guess the number between 1 and 9: "))
while str(user_guess) != "quit" :
    if user_guess == rand_num:
        print("you guessed {} you were right".format(user_guess))
    elif user_guess > rand_num:
        print("you guessed too high")
    else:
        print("you guessed too low")

    user_guess = int(input("Enter anoher guess or quit: "))
    
