from project.band_members.musician import Musician


class Singer(Musician):
    SKILLS = {
        "sing high pitch notes": ["Rock", "Jazz"],
        "sing low pitch notes": ["Metal", "Jazz"],
    }

    @staticmethod
    def check_skills():
        return Singer.SKILLS
