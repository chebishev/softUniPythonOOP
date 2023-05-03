class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        decoration = self.find_by_type(decoration.__class__.__name__)
        if decoration == "None":
            return False
        else:
            for d in self.decorations:
                if d == decoration:
                    self.decorations.remove(d)
                    return True

    def find_by_type(self, decoration_type):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        else:
            return "None"
