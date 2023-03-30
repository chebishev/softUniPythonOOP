from horse_racings.project import Band
from horse_racings.project import Drummer
from horse_racings.project import Guitarist
from horse_racings.project import Singer
from horse_racings.project import Concert


class ConcertTrackerApp:
    MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        if musician_type not in ConcertTrackerApp.MUSICIANS:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        else:
            musician = ConcertTrackerApp.MUSICIANS[musician_type](name, age)
            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        else:
            band = Band(name)
            self.bands.append(band)
            return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        else:
            concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert)
            return f"{genre} concert in {place} was added."

    def __find_band_by_name(self, name: str):
        for band in self.bands:
            if band.name == name:
                return band
        else:
            raise Exception(f"{name} isn't a band!")

    def add_musician_to_band(self, musician_name, band_name):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.__find_band_by_name(band_name)

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        band = self.__find_band_by_name(band_name)

        for member in band.members:
            if member.name == musician_name:
                band.members.remove(member)
                return f"{musician_name} was removed from {band_name}."
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place, band_name):
        band = self.__find_band_by_name(band_name)
        member_types = {m.__class__.__name__ for m in band.members}
        concert = [c for c in self.concerts if c.place == concert_place][0]

        if not member_types == set(self.MUSICIANS.keys()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for member in band.members:
            for skill, genres in member.SKILLS.items():
                for genre in genres:
                    if genre == concert.genre and skill not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
        else:
            profit = (concert.audience * concert.ticket_price) - concert.expenses

            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
