from horse_racings.project import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken:
                    room.take_room(people)
                    self.guests += room.guests
                    break

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    self.guests -= room.guests
                    room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
