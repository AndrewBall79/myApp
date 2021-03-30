class Cat:
    species = 'mammal'

    def __init__(self, name, age, weight, strike, gender, hp):
        self.name = name
        self.age = age
        self.weight = weight
        self.strike = strike
        self.gender = gender
        self.hp = hp


cat1 = Cat("Bootsie", 4, 7, 10, "Male", 10)
cat2 = Cat("Sophie", 9, 11, 8, "Female", 10)
cat3 = Cat("Ponce", 2, 7, 6, "Male", 10)


def get_oldest(*args):
    return max(args)
