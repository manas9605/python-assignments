'''Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.'''

d1={1:'man',2:'ram'}
d2={1:'dev',2:'son'}
d3={1:'ravi',2:'naman'}

final_dict = {1:d1,2:d2,3:d3}
print("final dictionary is : ",final_dict)