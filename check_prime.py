def checkPrime( num_list, number ):
    int_list = list(range(1,number+1))
    divisor_list = list()
    for num in int_list:
        if number % num == 0:
            divisor_list.append(num)

    list_len = len(divisor_list)
    print(list_len)

    if list_len == 2:
        return True
    else:
        return False


user_in = int( input( "Enter a number: " ) )

#create a list of numbers 1 throuhg the number that was input

list_num = list( range( 1,user_in + 1 ) )

if checkPrime(list_num, user_in):
    print("{} is prime".format(user_in))
else:
    print("{} not prime".format(user_in))
