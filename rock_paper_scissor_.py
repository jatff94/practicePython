def whoWins(pOne,pTwo):
    if pOne  == "rock":
        if pTwo =="rock":
            print("its a tie")
        elif pTwo =="paper" :
            print("paper beats rock - player two wins")
        else:
            print("Rock beats scissors - player one wins")

    elif pOne == "paper" :
        if pTwo == "rock":
            print("paper beats rock -- player one wins")
        elif pTwo == "paper":
            print("its a tie")
        else :
            print("scissors beats paper -- player two wins")

    else:
        if pTwo == "rock":
            print("rock beats scissors--player two wins")
        elif pTwo == "paper" :
            print("scissor beats paper --player two wins")
        else:
            print("Its a tie")


            
input_one = input("player one -  enter rock , paper, scissors, or quit: ")


while input_one != "quit" :
    input_two  = input("player two - rock , paper, scissors, or quit: ")
    if input_two == "quit" :
        break
    else:
        whoWins(input_one,input_two)

    input_one = input("enter another choice or quit: ")


print("Thanks for playing")
