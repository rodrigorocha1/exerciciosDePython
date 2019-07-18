print('Olá mundo')
help(print())
print(input.__doc__)


def contador(i, f, p):
    """[summary]

    Arguments:
        i {[type]} -- [description]
        f {[type]} -- [description]
        p {[type]} -- [description]
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


help(contador)


def somar(a, b, c=0):
    """[summary]

    Arguments:
        a {[type]} -- [description]
        b {[type]} -- [description]

    Keyword Arguments:
        c {int} -- [description] (default: {0})

    Returns:
        [type] -- [description]
    """
    s = a + b + c
    return s


somar(3, 4, 5)
somar(8, 2)
