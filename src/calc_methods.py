import math


# summ func: 1 + 1 -> 2
def summ(a: int, b: int) -> int:
    return a + b


# sub func: 1 - 1 -> 0
def sub(a: int, b: int) -> int:
    return a - b


# mult func: 2 * 2 -> 4
def mult(a: int, b: int) -> int:
    return a * b


# div func: 6 / 3 -> 2
def div(a: int, b: int) -> float:
    if b == 0:
        return 999999999999999999999
    return a / b


# mod func: 6 % 4 -> 2
def mod(a: int, b: int) -> int:
    if b == 0:
        return 999999999999999999998
    return a % b


# log2 func: log2(2) -> 1
def log2(a: int) -> float:
    if a > 0:
        return math.log2(a)
    return 999999999999999999999


# modulo func: abs(-2) -> 2
def modulo(a: int) -> int:
    return abs(a)
