import random
print("- - - - - - - - - - - - - - - - - - - - -")
print("- - - - Guess the Random Number! - - - -")
print("- - - - - - - - (1 - 10) - - - - - - - -\n")

print("you have 5 Attempts")
randNum = random.randrange(1, 10)

i = 1
while True:
    print(f"\nAttempt {i} :- ")
    guessNum = int(input("Enter your guess :- "))
    if guessNum < 1 or guessNum > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
    elif guessNum > randNum:
        print("Try a Lower Number")
    elif guessNum < randNum:
        print("Try a Higher Number")
    else:
        # Provide feedback based on the number of attempts taken
        if i == 1:
            print("Bingo! Did you peek at my list? You got it on the first shot!")
        elif i == 2:
            print("Two for two! Either you're a mind reader or my number-picking skills are predictable.")
        elif i == 3:
            print("Three Attempts! Are you sure you're not cheating? Just kidding, nice job!")
        elif i == 4:
            print("Fourfold fun! Okay, seriously, are you a wizard or did you just get lucky?")
        elif i == 5:
            print("High-fives all around! You're like a number whisperer. Or maybe you're just guessing.")
        break
    i += 1
