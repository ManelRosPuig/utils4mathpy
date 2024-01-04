from math import sqrt, ceil, isqrt
from typing import Optional

class Errors:
    ARGUMENT_NOT_VALID = "The argument must be an integer greater than 1"

class DivisorOptions:
    def __init__(self, limit: int = 0, reverse: bool = False, include_self: bool = True, include_one: True = False):
        self.limit = limit
        self.reverse = reverse
        self.include_self = include_self
        self.include_one = include_one

def divisors(n: int, opts: Optional[DivisorOptions] = DivisorOptions()) -> list[int]:

    if not isinstance(n, int) or n <= 1:
        raise TypeError(Errors.ARGUMENT_NOT_VALID)

    opts = opts or DivisorOptions()

    numbers = []

    if opts.include_one is True:
        numbers += [1]
    
    numbers += [i for i in range(2, n) if n % i == 0]

    if opts.include_self is True:
        numbers.append(n)
    
    if opts.reverse is True:
        numbers.sort(reverse = True)

    if opts.limit == 0:
        return numbers
    
    return numbers[:opts.limit]

def is_prime(n: int) -> bool:

    if not isinstance(n, int) or n <= 1:
        raise TypeError(Errors.ARGUMENT_NOT_VALID)
        
    for i in divisors(n, DivisorOptions(include_self = False)):
        if n % i == 0:
            return False

    return True

def factorize(n: int):
    numbers = divisors(n, limit = 1)
    for i in numbers:
        None

def sieve(n: int) -> list[int]:
    numbers = [i for i in range(2, n + 1)]
    for i in range(2, ceil(sqrt(n))):
        if numbers[i - 2] != 0:
            for j in range(i, ceil(n / i)):
                numbers[j * i - 2] = 0
    return [i for i in numbers if i != 0]
