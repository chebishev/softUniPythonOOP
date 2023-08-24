from collections import deque

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {
        'KneePad': KneePad,
        'ElbowPad': ElbowPad
    }

    VALID_TEAM_TYPES = {
        'IndoorTeam': IndoorTeam,
        'OutdoorTeam': OutdoorTeam
    }

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
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_EQUIPMENT_TYPES[equipment_type]())

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAM_TYPES[team_type](team_name, country, advantage))

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):

        for index in range(len(self.equipment) - 1, -1, -1):
            current_equipment = self.equipment[index]
            if current_equipment.__class__.__name__ == equipment_type:
                buying_team = [team for team in self.teams if team.name == team_name][0]
                if current_equipment.price > buying_team.budget:
                    raise Exception("Budget is not enough!")

                buying_team.equipment.append(self.equipment.pop(index))
                buying_team.budget -= current_equipment.price

                return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        try:
            team = [team for team in self.teams if team.name == team_name][0]
        except IndexError:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        counter = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1, team_name2):
        teams = deque([[team for team in self.teams if team.name == team_name1][0],
                       [team for team in self.teams if team.name == team_name2][0]])

        if teams[0].__class__.__name__ != teams[1].__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        while teams[0].result() != teams[1].result():
            team_one = teams[0]
            team_two = teams[1]
            if team_one.result() > team_two.result():
                team_one.win()
                return f"The winner is {team_one.name}."

            teams.rotate()

        else:
            return "No winner in this game."

    def get_statistics(self):
        output = [f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"]
        for team in sorted(self.teams, key=lambda x: -x.wins):
            output.append(team.get_statistics())
        return '\n'.join(output)


# test inputs:

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
