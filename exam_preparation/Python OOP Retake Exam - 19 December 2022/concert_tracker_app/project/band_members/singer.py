from project.band_members.musician import Musician


class Singer(Musician):
    SKILLS = {
        "sing high pitch notes": ["Rock", "Jazz"],
        "sing low pitch notes": ["Metal", "Jazz"],
    }

    def check_skills(self):
        return Singer.SKILLS
