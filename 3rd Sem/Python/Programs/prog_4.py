print("A Program to check weather a Input number is prime or not using for loop\n")
num = int(input("Enter a Integer value :- "))
if num <= 1:
    print("Not prime")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not prime")
            break 
    else:
        print("Prime")