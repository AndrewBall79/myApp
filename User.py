
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f'attacking with {self.num_arrows}')


wizard1 = Wizard('Merlin', 50, "email")
archer1 = Archer('Arrow', 100, "email")


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

print(wizard1.email)
