class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.step * self.index


# test inputs:

# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
