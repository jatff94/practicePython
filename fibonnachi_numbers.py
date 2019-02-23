def fib_sequence(fib_num):
    list_fib = list()
    count = 0
    while count < int(fib_num) :
        if count == 0 or count == 1:
            list_fib.append(1)
        else:
            list_fib.append(list_fib[count-2] + list_fib[count-1])
        count+=1
    print(list_fib)

fib_num = input("Enter how many fibonnachi numbers to generate")

fib_sequence(fib_num)

