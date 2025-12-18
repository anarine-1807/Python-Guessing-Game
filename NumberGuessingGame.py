import random


def play_number_guessing_game():


print("Pick a number between 1 and 100.")

special_number = random.randint(1, 100)

attempts = 0
guess = 0

while guess != special_number:
    try:
        guess = int(input("Guess a number"; ))
        attempts += 1

        if guess < special_number
            print("Sorry, too low, try again.")
        elif guess > special_number
            print("Sorry, too high, try again.")
            else
            print("Congratulations, you guessed it correct!")
        except error
    print("Invalid, please enter a whole number.")

if __name__ = "__main__":
    play_number_guessing_game()
