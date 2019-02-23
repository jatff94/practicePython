self = {"height":5.5, "color":"red","author":"Steinbeck"}

user_in = input("what do you want to know about me? :")

if user_in in self :
    print(str(self[user_in]))
else:
    print("enter a valid key")
    
music_list = {
    "Pink Floyd":["Have a cigar","The wall"],
    "Sublime":["Santaria","Bad fish", "Scarlet begonias"]
    }
