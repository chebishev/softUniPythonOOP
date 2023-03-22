from itertools import permutations


def possible_permutations(args):
    if len(args) == 1:
        yield args
    else:
        for permutation in permutations(args):
            yield list(permutation)

# test inputs:
# [print(n) for n in possible_permutations([1, 2, 3])]
#
# [print(n) for n in possible_permutations([1])]
