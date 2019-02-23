list_one = [1,1,3,4,5,6,7,5,6,7,56]
list_two = [2,56,2,5,4,]
list_similar = []

for num_one in list_one:
    for num_two in list_two:
        if num_one in list_two:
            if num_one not in list_similar:

                list_similar.append(num_one)

print(list_similar)
