import string
from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
your_list = [9, 10, 11, 12, 13, 14, 15, 16]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# print(list(filter(check_odd, my_list)))
# print(list(map(multiply_by2, my_list)))
# print(list(map(lambda item: item * 2, my_list)))
# print(list(zip(my_list, your_list)))
# print(reduce(accumulator, my_list, 0))
# print(reduce(lambda acc, item: acc + item, my_list))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


# print(string.ascii_letters)
def to_capital(item):
    return item.upper()


# print(list(map(to_capital, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_numbers = [5, 4, 3, 2, 1]


def sort(item):
    return sorted(item)


# print(list(zip(sort(my_list), my_strings)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def check_pass(item):
    return item >= 50


# print(list(filter(check_pass, scores)))

# Lambda to the power of x
powers_list = [5, 4, 3]

# print(list(map(lambda num: pow(num, 2), powers_list)))

# list Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
# print(a)

# list, set, dictionary Comprehensions

my_comprehensive_list = [char for char in "hello"]
my_comprehensive_list2 = [num for num in range(0, 100)]
my_comprehensive_list3 = [num * 2 for num in range(0, 100)]
my_comprehensive_set = {num ** 2 for num in range(0, 100) if num % 2 == 0}
simple_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
my_dictionary = {key: value ** 2 for key, value in simple_dictionary.items() if value % 2 == 0}

my_dictionary2 = {my_pets[num - 1]: num for num in range(1, 5)}
# print(my_dictionary2)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

# print(duplicates)


def my_decorator(func):
    def wrap_func(*x, **y):
        print('*****')
        func(*x, **y)
        print('*****')
    return wrap_func


@my_decorator
def hello(*args, emoji=":("):
    print(*args, emoji)


hello("hi", ':(', 'chosen')
