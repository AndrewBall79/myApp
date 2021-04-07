def do_stuff(number=0):
    try:
        if number:
            return int(number) + 5
        else:
            return "Please Enter Number"
    except ValueError as err:
        return err


