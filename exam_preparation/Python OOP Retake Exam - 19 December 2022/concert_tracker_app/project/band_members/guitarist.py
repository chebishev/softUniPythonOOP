from horse_racings.project import Musician


class Guitarist(Musician):
    SKILLS = {
        "play rock": ["Rock"],
        "play metal": ["Metal"],
        "play jazz": ["Jazz"]
    }

    @staticmethod
    def check_skills():
        return Guitarist.SKILLS
