from cats import cat1


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='Anonymous', color='grey', age=18, attack=10):
        if age > 18:
            self.name = name
            self.color = color
            self.age = age
            self.attack = attack

    def shout(self):
        print(f'My name is {self.name}!')

    def run(self):
        print(f'{self.name} is running!')

    def kill(self):
        print(f'I am {self.name} and I\'m ready to kill')

    @classmethod
    def adding_things(cls, num1, num2, num3, num4):
        return cls("Abbie", 'blue', num1 + num2, num3 + num4)

    @staticmethod
    def adding_things2(num3, num4):
        return


player1 = PlayerCharacter('Andy', 'blue', 22, 10)
player2 = PlayerCharacter('Tom', 'red', 54, 8)
player3 = PlayerCharacter.adding_things(14, 6, 5, 2)
all_players = {
    player1,
    player2,
    player3
}
for player in all_players:
    pass
    print(f"{player.name} is {player.color} their age is {player.age} their attack power is {player.attack}.")
    print(cat1.name)
    # print(player.shout())
    # print(player.run())
    # print(player.kill())
