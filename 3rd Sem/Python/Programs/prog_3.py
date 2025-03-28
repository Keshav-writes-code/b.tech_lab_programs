
print("---------------------")
print("A Program to check whether an input number is prime or not using for loop\n")

# Prompt the user for another input
num = int(input("Enter a value: "))
exists = False

# Check if the input number is less than 2
if num < 2:
    # Loop through a range of numbers to check for factors
    for x in range(2, int(num/2)):
        if num % x == 0:
            exists = True
            break

    print("")

    # Print whether the number is prime or not
    if exists:
        print("It's not a prime number")
    else:
        print("It's a prime number")
# If the input number is greater than or equal to 0, it's not prime
elif num >= 0:
    print("It's not a prime number")
