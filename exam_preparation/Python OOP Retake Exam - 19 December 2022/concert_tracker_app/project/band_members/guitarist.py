from project.band_members.musician import Musician


class Guitarist(Musician):
    SKILLS = {
        "play rock": ["Rock"],
        "play metal": ["Metal"],
        "play jazz": ["Jazz"]
    }

    def check_skills(self):
        return Guitarist.SKILLS
