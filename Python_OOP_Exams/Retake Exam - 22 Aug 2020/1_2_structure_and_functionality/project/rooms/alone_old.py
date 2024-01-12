from project.rooms.room import Room


class AloneOld(Room):
    room_cost = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, 1)
        self.room_cost: int = AloneOld.room_cost
