class Tournament:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):
        pass

    def add_team(self, team_type, team_name, country, advantage):
        pass

    def sell_equipment(self, equipment_type, team_name):
        pass

    def remove_team(self, team_name):
        pass

    def increase_equipment_price(self, equipment_type):
        pass

    def play(self, team_name1, team_name2):
        pass

    def get_statistics(self):
        pass

# test input:

# t = Tournament('SoftUniada2023', 2)
#
# print(t.add_equipment('KneePad'))
# print(t.add_equipment('ElbowPad'))
#
# print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
# print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
# print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))
#
# print(t.sell_equipment('KneePad', 'Spartak'))
#
# print(t.remove_team('Levski'))
# print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))
#
# print(t.increase_equipment_price('ElbowPad'))
# print(t.increase_equipment_price('KneePad'))
#
# print(t.play('Lokomotiv', 'Spartak'))
#
# print(t.get_statistics())
