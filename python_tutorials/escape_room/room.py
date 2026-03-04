class Room:

    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, entered_code):
        return self.escape_code == entered_code

    def get_game_object_names(self):
        object_names = []
        for i in self.game_objects:
            object_names.append(i.name)

        return object_names

### Unit test for room class
from game_object import GameObject

class RoomTests:
    def __init__(self):
        self.room_1 = Room(111, [GameObject("Sweater", "It's a blue sweater that had the number 12 stitched on it.",
                   "someone has unstitched a second number, leaving only the 1",
                   "the sweater smells of laundry detergent"),
        GameObject("Chair", "It's a wood chair with only 3 legs.",
                   "Someone has snapped off one leg.", "It smells like old wood.")])
        self.room_2 = Room(222, [])

    def test_check_code(self):
        print(self.room_1.check_code(111) == True)
        print(self.room_1.check_code(222) == False)

    def check_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ["Sweater", "Chair"])
        print(self.room_2.get_game_object_names() == [])

#tests = RoomTests()
#tests.test_check_code()
#tests.check_get_game_object_names()