import random

secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20. Can you guess what it is? I'll give you five tries.")

for guesses_taken in range(1, 6):
    print("Take a guess.")
    try:
        guess = int(input())
        if 1 <= guess <= 20:
            if secret_number > guess:
                print("Your guess was too low.")
            elif secret_number < guess:
                print("Your guess was too high.")
            else:
                break
        else:
            print("Your guess is out of range. Please enter a number between 1 and 20")
    except ValueError:
        print("Please enter a number, not a word")

if guess == secret_number:
    print("You got it! You guessed the correct number in " + str(guesses_taken) + " tries!")
else:
    print("You're out of guesses! Sorry, the number was " + str(secret_number) + ".")
