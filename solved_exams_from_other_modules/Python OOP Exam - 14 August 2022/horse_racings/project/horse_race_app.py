from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def get_jockey(self, name):
        try:
            jockey = [j for j in self.jockeys if j.name == name][0]
        except IndexError:
            raise Exception(f"Jockey {name} could not be found!")

        return jockey

    def get_race(self, race_type):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        return race

    def add_horse(self, horse_type, horse_name, horse_speed):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSES:
            horse = self.VALID_HORSES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):

        jockey = self.get_jockey(jockey_name)

        if horse_type not in self.VALID_HORSES:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        for horse in self.horses[::-1]:

            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                if jockey.horse is not None:
                    return f"Jockey {jockey_name} already has a horse."

                jockey.horse = horse
                horse.is_taken = True

                return f"Jockey {jockey_name} will ride the horse {horse.name}."

        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):

        race = self.get_race(race_type)
        jockey = self.get_jockey(jockey_name)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for j in race.jockeys:
            if j.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race.race_type} race."

        if jockey.horse is not None:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race.race_type} race."

    def start_horse_race(self, race_type):
        race = self.get_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest_jockey = ""
        fastest_horse = ""
        fastest_horse_speed = -1
        for jockey in race.jockeys:
            if jockey.horse.speed > fastest_horse_speed:
                fastest_horse_speed = jockey.horse.speed
                fastest_horse = jockey.horse.name
                fastest_jockey = jockey.name

        return f"The winner of the {race_type} race, with a speed of {fastest_horse_speed}km/h" \
               f" is {fastest_jockey}! Winner's horse: {fastest_horse}."
