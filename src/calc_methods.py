# summ func: 1 + 1 -> 2
def summ(a: int, b: int) -> int:
    return a + b


# sub func: 1 - 1 -> 0
def sub(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    if b == 0:
        return 999999999999999999999
    return a / b


def mod(a: int, b: int) -> int:
    if b == 0:
        return 999999999999999999998
    return a % b
