from horse_racings.project import Reptile
from horse_racings.project import Mammal
from horse_racings.project import Lizard


class Snake(Reptile):
    pass


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
