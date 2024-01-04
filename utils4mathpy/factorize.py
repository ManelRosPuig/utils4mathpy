from utils4mathpy import divisors, invalid_int_greater_than
from utils4mathpy.divisors_options import DivisorsOptions

def factorize(n: int):
    smallest_divisor = divisors(n, DivisorsOptions(limit = 1))[0]
    next = int(n / smallest_divisor)
    if next == 1:
        return [smallest_divisor]
    else:
        return [smallest_divisor] + factorize(next)

print(factorize(2))
