from project.booths.booth import Booth


class OpenBooth(Booth):
    def __init__(self, boot_number, capacity):
        super().__init__(boot_number, capacity)

    def reserve(self, number_of_people):
        pass
