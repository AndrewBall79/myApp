from cats import *
from player import *


class App:

    print(f"The oldest cat, {get_oldest(cat1.name, cat2.name, cat3.name)} is {get_oldest(cat1.age, cat2.age, cat3.age)} years old.")
    for player in all_players:
        print(f"{player.name} is {player.color} their age is {player.age} their attack power is {player.attack}.")


