num_input = int(input("enter a number: "))

if num_input <= 10 :
    print(str(num_input) + " less than or equal to 10" )
elif num_input > 10 and num_input <=25:
    print(str(num_input) + " greater than 10 but less than 25" )
elif num_input > 25 :
    print(str(num_input) + " greater than 25 ")
    

num_one = int(input("1st number: "))
num_two = int(input("2nd number: "))

remainder = num_one % num_two

print("The remainder of " + str(num_one) + " and " + str(num_two) + \
      "is " + str(remainder))
