import coverage

from utils4mathpy import divisors, is_prime, DivisorOptions

print(divisors(3, DivisorOptions(
    limit = 0,
    reverse = False,
    include_self = True,
    include_one = True
)))
