class Monsters:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    species = 'mammal'
    is_lazy = True

    def __init__(self, name, age, weight, strike, gender, hp):
        self.name = name
        self.age = age
        self.weight = weight
        self.strike = strike
        self.gender = gender
        self.hp = hp

    def walk(self):
        print(f'{self.name} is just walking around')


cat1 = Cat("Bootsie", 4, 7, 10, "Male", 10)
cat2 = Cat("Sophie", 9, 11, 8, "Female", 10)
cat3 = Cat("Ponce", 2, 7, 6, "Male", 10)


def get_oldest(*args):
    return max(args)


my_cats = {
    cat1,
    cat2,
    cat3
}

