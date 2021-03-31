
class User:

    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f'attacking with {self.num_arrows}')

    def run(self):
        print('runs fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        super().__init__(name, power)


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Arrow', 100)
hb1 = HybridBorg('Rob0L0', 89)


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
hb1.run()
