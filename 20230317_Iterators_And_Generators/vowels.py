class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = 'aeiouy'

    def __iter__(self):
        return self

    def __next__(self):
        if self.text:
            word = self.text[0]
            self.text = self.text[1:]
            if word.lower() in self.vowels:
                return word
            else:
                return next(self)
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
