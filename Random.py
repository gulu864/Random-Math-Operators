import random
print("Welcome to the guess the number game")
print("Instructions: i'll guess a number 1 to 10 and you have to guess it!")
var=random.randint(1,10)
while True:
    guess=int(input("Enter your guess:"))
    if var < guess:
        print("Your guess is higher.")
    elif var > guess:
        print("Your guess is lower.")
    elif var == guess:
        print("You gussed the number correctly!")
        break
    else:
        print("invalid option")

print("Thank you for playing")