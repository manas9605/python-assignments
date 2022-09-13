'''Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''

s1 = input("what is your favourite colour : ")
l1=["Yellow","Blue","Orange","White","Black","Red"]
for colour in l1:
    if colour in s1:
        c=colour
        break
else:
    c="other"
match c:
    case "Yellow":
        print("monday")
    case "Blue":
        print("tuesday")
    case "Orange":
        print("wednesday")
    case "White":
        print("thursday")
    case "Black":
        print("friday")
    case "Red":
        print("saturday")
    case "other":
        print("sunday")