import cats
import player
from cats import *
from player import *


class App:
    # print(f"The oldest cat, {get_oldest(cat1.name, cat2.name, cat3.name)} is {get_oldest(cat1.age, cat2.age, cat3.age)} years old.")
    for player in all_players:
        if player.gender == 'M':
            gender_call = 'his'
        else:
            gender_call = 'her'
        # print(f"{player.name} is {player.color} {gender_call} age is {player.age} {gender_call} attack power is {player.attack}.")


def player_vs_enemy():
    if cat1.hp - player1.attack <= 0:
        print(f"{cat1.name} has been killed")
    else:
        print(f"{player1.name} has been killed!")


# player_vs_enemy()



