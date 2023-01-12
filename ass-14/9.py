'''Write a Python script to print indices of all occurrences of a given element in a given
list.'''
my_list = [1, 2, 3, 1, 5, 4]
item = 1

indices = [i for i in range(len(my_list)) if my_list[i] == item]

print(indices)
