def vowel_filter(function):
    def wrapper():
        return [ch for ch in function() if ch in "aeiouAEIOU"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
