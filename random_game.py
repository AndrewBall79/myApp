from random import *

user_number = input("How large do you want your range?: ")

number_range = range(1, int(user_number))

guess_me = choice(number_range)

print(guess_me)

while True:
    try:
        user_guess = int((input(f"Guess a number between 1 and {user_number}: ")))
        if 0 < user_guess > int(user_number):
            print("Stay in your range!!")
        if user_guess != guess_me:
            print("Try again")
        else:
            print("You guessed correctly")
            break
    except ValueError:
        print("please enter a real number")
        continue

