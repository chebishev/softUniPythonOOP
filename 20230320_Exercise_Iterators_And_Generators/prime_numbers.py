import math


def get_primes(numbers):
    for number in numbers:
        if number > 1:
            for i in range(2, int(math.sqrt(number) + 1)):
                if (number % i) == 0:
                    break
            else:
                yield number

# test inputs:
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# print(list(get_primes([-2, 0, 0, 1, 1, 0])))
