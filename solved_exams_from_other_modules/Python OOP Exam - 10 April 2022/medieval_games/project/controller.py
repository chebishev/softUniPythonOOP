class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        result = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                result.append(player.name)
        return f"Successfully added: {', '.join(result)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def sustain(self, player_name, sustenance_type):

        if not self.find_player_by_name(player_name):
            return
        else:
            player = self.find_player_by_name(player_name)

        if sustenance_type not in ("Food", "Drink"):
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if not [x for x in self.supplies if x.__class__.__name__ == sustenance_type]:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == sustenance_type:
                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy

                self.supplies.pop(index)

                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)

        if first_player.stamina <= 0 and second_player.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        elif first_player.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."

        players = sorted([first_player, second_player], key=lambda p: -p.stamina)

        for _ in range(2):
            attacker_one = players.pop()
            attacker_two = players.pop()
            attacker_one.hit = attacker_one.stamina / 2
            if attacker_two.stamina - attacker_one.hit <= 0:
                attacker_two.stamina = 0
                return f"Winner: {attacker_one.name}"

            attacker_two.stamina -= attacker_one.hit
            players = [attacker_one, attacker_two]

        else:
            nax_stamina = -1
            player_name = ""
            for player in players:
                if player.stamina > nax_stamina:
                    nax_stamina = player.stamina
                    player_name = player.name
            return f"Winner: {player_name}"

    def next_day(self):
        for player in self.players:
            stamina_to_decrease = player.age * 2
            if player.stamina - stamina_to_decrease < 0:
                player.stamina = 0
            else:
                player.stamina -= stamina_to_decrease
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = []
        for player in self.players:
            output.append(str(player))
        for supply in self.supplies:
            output.append(supply.details())
        return "\n".join(output)
