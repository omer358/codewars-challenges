def make_negative(number):
    if number == 0:
        return 0
    elif number > 0:
        return number - (number + number)
    else:
        return number


print(make_negative(3))
