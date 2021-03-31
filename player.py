class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, gender, name='Anonymous', color='grey', age=18, attack_power=10):
        if age > 18:
            self.gender = gender
            self.name = name
            self.color = color
            self.age = age
            self.attack_power = attack_power

    def shout(self):
        print(f'My name is {self.name}!')

    def run(self):
        print(f'{self.name} is running!')

    def kill(self):
        print(f'I am {self.name} and I\'m ready to kill')

    def suicide(self):
        print(f"{self.name} has killed themself.")

class Wizard(PlayerCharacter):
    def __init__(self, power, magic_type, gender, name, color, age, attack_power):
        super().__init__(gender, name, color, age, attack_power)
        self.power = power
        self.magic_type = magic_type

    def attack(self):
        print(f'attacking with power of {self.magic_type}')


class Archer(PlayerCharacter):
    def __init__(self, num_arrows, arrow_type, gender, name, color, age, attack_power):
        super().__init__(gender, name, color, age, attack_power)
        self.num_arrows = num_arrows
        self.arrow_type = arrow_type

    def attack(self):
        print(f'attacking with {self.arrow_type}')


class Warrior(PlayerCharacter):
    def __init__(self, weapon_strength, weapon_type, gender, name, color, age, attack_power):
        super().__init__(gender, name, color, age, attack_power)
        self.weapon_strength = weapon_strength
        self.weapon_type = weapon_type

    def attack(self):
        print(f'attacking with {self.weapon_type}')


player1 = Warrior(20, "Sword", 'M', 'Andy', 'blue', 44, 10)
player2 = Warrior(24, "Mace", 'M', 'Tom', 'red', 54, 8)
player3 = Archer(15, "Ice", 'F', "Abbie", 'blue', 22, 15)
player4 = Wizard(50, 'Fire', 'F', "Elviwn", 'grey', 250, 18)
all_players = {
    player1,
    player2,
    player3,
    player4
}


