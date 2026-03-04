from room import Room
from game_object import GameObject

class Game:

    def __init__(self, objects):
        self.attempts = 0
        self.objects = objects
        self.room = Room(731, objects)

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection: int = int(input(prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection - 1)
        self.take_turn()

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt

    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    def get_object_interaction_string(self, name):

        return (f"How do you want to interact with {name}?\n"
                f"1. Look\n2. Touch\n3. Smell\n")

    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
