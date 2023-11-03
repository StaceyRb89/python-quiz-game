import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ("Please choose a number large than 0")
        quit()
else:
    print ("Please type a number next time")
    quit()
"""have to include top and bottom of the range for it to work, you can also use
random.randrange with 0-5 and it wont give you those numbers just the ones within it"""
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess == "quit":
        print("You chose to quit!")
        quit()
    else:
        print("Please type a number next time :)")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses!") 