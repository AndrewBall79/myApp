
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, gender, name='Anonymous', color='grey', age=18, attack=10):
        if age > 18:
            self.gender = gender
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


class Wizard(PlayerCharacter):
    def __init__(self, power, magic_type, gender, name, color, age, attack):
        super().__init__(gender, name, color, age, attack)
        self.power = power
        self.magic_type = magic_type

    def attack(self):
        print(f'attacking with power of {self.magic_type}')


class Archer(PlayerCharacter):
    def __init__(self, num_arrows, arrow_type, gender):
        super().__init__(gender)
        self.num_arrows = num_arrows
        self.arrow_type = arrow_type

    def attack(self):
        print(f'attacking with {self.num_arrows}')


player1 = PlayerCharacter('M', 'Andy', 'blue', 44, 10)
player2 = PlayerCharacter('M', 'Tom', 'red', 54, 8)
player3 = PlayerCharacter('F', "Abbie", 'blue', 22, 15)
player4 = Wizard(50, 'Fire', 'F', "Elviwn", 'grey', 250, 18)
all_players = {
    player1,
    player2,
    player3,
    player4
}


print(player4.shout())
