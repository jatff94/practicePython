def list_to_set(reg_list):
    return set(reg_list)

def list_loop(reg_list):
    nl = list()
    for element in reg_list:
        if element not in nl:
            nl.append(element)
    return nl

    
l = ["mark","mark","luis","juan","raul","juan"]
o = [1,2,5,1,7,9,1,2,5]
print(list_to_set(l))

print(list_loop(o))
