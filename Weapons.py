class Weapon:
    def __init__(self, color, age, power):
        self.color = color
        self.age = age
        self.power = power

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5


black_sword = Weapon('black', 1000, 15)
red_sword = Weapon('red', 1000, 15)

print(black_sword.__str__())
print(red_sword.__str__())
