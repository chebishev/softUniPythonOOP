class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        ...

    def add_jockey(self, jockey_name, age):
        ...

    def create_horse_race(self, race_type):
        ...

    def add_horse_to_jockey(self, jockey_name, horse_type):
        ...

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        ...

    def start_horse_race(self, race_type):
        ...

    