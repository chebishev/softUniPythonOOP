def cache(func):
    log = {}

    def wrapper(args):
        if args not in log:
            log[args] = func(args)
        return log[args]

    wrapper.log = log

    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
