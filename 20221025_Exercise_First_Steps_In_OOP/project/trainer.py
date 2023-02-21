from pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.pokemons = []
        self.name = name

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in self.pokemons:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon_name)
        return f"You have released {pokemon_name}"

    def trainer_data(self):

        output = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]

        for element in self.pokemons:
            output.append(f"- {element.pokemon_details()}")

        return '\n'.join(output)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
