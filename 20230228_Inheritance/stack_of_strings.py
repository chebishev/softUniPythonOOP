class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop() if self.data else None

    def top(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(element for element in self.data[::-1])}]"
