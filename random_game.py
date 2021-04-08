from random import *


def run_random_game(user_guess, answer, user_range):
    if 0 < user_guess > int(user_range):
        print("Stay in your range!!")
    if user_guess != answer:
        print("Try again")
    else:
        print("You guessed correctly")
        return True


if __name__ == '__main__':
    user_range = input("How large do you want your range?: ")
    number_range = range(0, int(user_range))
    answer = choice(number_range)
    print("Your number is " + str(answer))
    while True:
        try:
            user_guess = int(input(f"Guess a number between 0 and {user_range}: "))
            if run_random_game(user_guess, answer, user_range):
                break
        except ValueError:
            print("please enter a real number")
            continue


