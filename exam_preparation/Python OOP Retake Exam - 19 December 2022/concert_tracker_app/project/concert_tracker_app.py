class ConcertTrackerApp:
    MUSICIAN_TYPES = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in ConcertTrackerApp.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        else:
            musician = musician_type(name, age)
            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name):
        pass

    def add_musician_to_band(self, musician_name, band_name):
        pass

    def remove_musician_from_band(self, musician_name, band_name):
        pass

    def start_concert(self, concert_place, band_name):
        pass
