import re

regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
regex_pass = r'[a-zA-Z0-9!@#$%^&*()]{8,}\d'


def check(email):
    if re.search(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")


def check_pass(password):
    if re.search(regex_pass, password):
        print("Valid Password")
    else:
        print("Invalid Password")


if __name__ == '__main__':
    email = "someemail@gmail.com"
    password = 'aArde!@12'

    check(email)
    check_pass(password)
