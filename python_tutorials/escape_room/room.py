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
