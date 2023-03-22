def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


# test inputs:
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))

# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
