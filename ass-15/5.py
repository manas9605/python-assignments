'''Write a python script to get the count of total number of characters in String a=
“iNeuron”'''
a='iNeuron'
count=0
for i in range(0,len(a)):
    if a[i]!='':
        count+=1
print("total nos of characters in string a is : ",count)