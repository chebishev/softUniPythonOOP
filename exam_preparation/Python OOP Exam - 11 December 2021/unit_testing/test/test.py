from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")

    def test_initialization(self):
        self.assertEqual(self.team.name, "Team")
        self.assertEqual(self.team.members, {})

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            team = Team("te4m")
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        self.team.add_member(**{"John": 25})
        self.assertEqual(self.team.members, {"John": 25})

    def test_ass_member_existing(self):
        self.team.add_member(**{"John": 25})
        self.team.add_member(**{"John": 26})
        self.assertEqual(self.team.members, {"John": 25})

    def test_remove_member_existing(self):
        self.team.add_member(**{"John": 25})
        self.team.add_member(**{"Johnny": 26})
        self.assertEqual(self.team.remove_member("John"), "Member John removed")
        self.assertEqual(self.team.members, {"Johnny": 26})

    def test_remove_member_unexisting(self):
        self.team.add_member(**{"John": 25})
        self.team.add_member(**{"Johnny": 26})
        self.assertEqual(self.team.remove_member("Johann"), "Member with name Johann does not exist")
        self.assertEqual(self.team.members, {"John": 25, "Johnny": 26})

    def test__gt__method_false(self):
        team = Team("Teams")
        team.add_member(**{"John": 25, "Johnny": 26, "Pete": 27})
        self.assertEqual(self.team.__gt__(team), False)

    def test__gt_method_true(self):
        new_team = Team("Teams")
        self.team.add_member(**{"John": 25, "Johnny": 26, "Pete": 27})
        self.assertEqual(self.team.__gt__(new_team), True)

    def test__len__method(self):
        self.assertEqual(len(self.team), 0)
        self.assertEqual(self.team.members, {})

    def test__add__method(self):
        new_team = Team("Teams")
        self.team.add_member(**{"John": 25, "Johnny": 26, "Pete": 27})
        new_team.add_member(**{"Ivan": 5, "Peter": 27})
        added_team = self.team + new_team
        self.assertEqual(added_team.name, "TeamTeams")
        self.assertEqual(added_team.members, {"John": 25, "Johnny": 26, "Pete": 27, "Ivan": 5, "Peter": 27})
        self.assertEqual(len(added_team), 5)

    def test__str__method(self):
        self.team.add_member(**{"John": 25, "Johnny": 26, "Pete": 27})
        self.assertEqual(str(self.team), "Team name: Team\n"
                                         "Member: Pete - 27-years old\n"
                                         "Member: Johnny - 26-years old\n"
                                         "Member: John - 25-years old")


if __name__ == "__main__":
    main()
