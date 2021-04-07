import re

pattern = re.compile(r'[a-zA-Z]+/')
string = 'B4nn4puDD!?'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a, b, c, d)
