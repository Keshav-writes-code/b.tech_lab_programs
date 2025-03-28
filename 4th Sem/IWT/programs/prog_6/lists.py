# To swap two element in a list
list1 = [int(input("1 :- ")), int(input("2 :- "))]
print("Original :- ",list1)

# ways to check if an element exists in a list
a = int(input("Give a value to check in the List :- "))
if a in list1:
    print("'",a,"' Exists in the List")
else:
    print("'",a,"' Doesn't Exists in the List")