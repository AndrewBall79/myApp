from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
your_list = [9, 10, 11, 12, 13, 14, 15, 16]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print(list(filter(check_odd, my_list)))
print(list(map(multiply_by2, my_list)))
print(list(map(lambda item: item*2, my_list)))
print(list(zip(my_list, your_list)))
print(reduce(accumulator, my_list, 0))
print(reduce(lambda acc, item: acc+item, my_list))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def to_capital(item):
    return item.upper()


print(list(map(to_capital, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


def sort(item):
    return sorted(item)


print(list(zip(sort(my_list), my_strings)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def check_pass(item):
    return item >= 50


print(list(filter(check_pass, scores)))
