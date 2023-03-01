class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        self.seconds += 1
        self.hours, self.minutes, self.seconds = self.check_time(self.seconds, self.minutes, self.hours)
        return self.get_time()

    def check_time(self, seconds, minutes, hours):
        if seconds > Time.max_seconds:
            seconds = 0
            minutes += 1
            if minutes > Time.max_minutes:
                minutes = 0
                hours += 1
                if hours > Time.max_hours:
                    hours = 0
        return hours, minutes, seconds


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
