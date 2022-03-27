# learning about infinite number of function arguments


def add(*args):
    _sum = 0
    for num in args:
        _sum += num
    return _sum


print(add(1,2,11,0, 100))
