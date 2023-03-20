from project.band_members.musician import Musician


class Drummer(Musician):

    SKILLS = {
        "play the drums with drumsticks": ["Rock", "Metal"],
        "play the drums with drum brushes": ["Jazz"],
        "read sheet music": []
                       }

    def check_skills(self):
        return Drummer.SKILLS
