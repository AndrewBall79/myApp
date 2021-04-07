from translate import Translator

translator = Translator(to_lang='fr')
try:
    with open('testo.txt', 'r') as my_file:
        text = my_file.read()
        print(translator.translate(text))
        with open('text_fr_translate.txt', 'a') as my_file2:
            print(my_file2)
except FileNotFoundError as err:
    print('Filo no existo')
    raise err
except IOError as err:
    print('IO error')
    raise err




