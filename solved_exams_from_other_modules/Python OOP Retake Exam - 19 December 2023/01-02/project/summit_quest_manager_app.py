from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    CONQUERED_PEAKS = set()

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."
        for climber in self.climbers:
            if climber.name == climber_name:
                return f"{climber_name} has been already registered."
        self.climbers.append(self.VALID_CLIMBERS[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."
        self.peaks.append(self.VALID_PEAKS[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        if peak.get_recommended_gear() == gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        result = set(peak.get_recommended_gear()).difference(set(gear))
        climber.is_prepared = False
        missing_gear = sorted(list(result))
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = [c for c in self.climbers if c.name == climber_name][0]
        except IndexError:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = [p for p in self.peaks if p.name == peak_name][0]
        except IndexError:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            self.CONQUERED_PEAKS.add(peak_name)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        output = f"Total climbed peaks: {len(self.CONQUERED_PEAKS)}\n**Climber's statistics:**"
        for climber in sorted(self.climbers, key=lambda c: (-(len(c.conquered_peaks)), c.name)):
            if climber.conquered_peaks:
                output += "\n" + str(climber)
        return output
