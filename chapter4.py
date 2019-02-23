def num_squared(x) :
    return x**2

def print_string(string):
    print(string)

def req_and_opt(x,y,z,w=1,k=2):
    return x+y+z+w+k

def divide_by_two(num):
    return num/2

def mul_by_four(num):
    return num * 4

def convert_float(converter):
    return float(converter) 

print(str(num_squared(4)))
print_string("Hey hoe")
return_num = divide_by_two(4)
print(str(mul_by_four(return_num)))

try :
    convert_float("hey")

except ValueError:
    print("you need to enter a valid float number")
