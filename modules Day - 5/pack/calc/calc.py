def add(*args):
    return sum(args)


def mul(*args):
    total = 1

    for elem in args:
        total *= elem
    return total


def sub(x, y):
    return x - y


def div(x, y):
    return x/y