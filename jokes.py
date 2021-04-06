import pyjokes
from collections import Counter, defaultdict, OrderedDict

print(pyjokes.get_joke())

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Counter(li))

dictionary = defaultdict(lambda: 5, {"a": 1, "b": 2})
print(dictionary['c'])
