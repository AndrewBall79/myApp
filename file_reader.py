try:
    with open('test.txt', 'a') as my_file:
        print(my_file.write(""))
except FileNotFoundError as err:
    print('Filo no existo')
    raise err
except IOError as err:
    print('IO error')
    raise err


