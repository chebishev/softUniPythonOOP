def solution():

    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in seq:
            if len(result) == n:
                return result
            result.append(i)

    return take, halves, integers


# test inputs:
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))

# take = solution()[0]
# halves = solution()[1]
# print(take(0, halves()))
