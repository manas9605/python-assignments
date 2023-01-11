'''Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}'''
sample_dict = {'C': 92,'Java': 66,'Python': 85}
b=min(sample_dict, key=sample_dict.get())
print(b)
