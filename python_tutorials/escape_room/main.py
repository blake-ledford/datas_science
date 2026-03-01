#this will be where everything gets implemented
from game import Game
from game_object import GameObject
from room import Room

instructions = ("You are in an escape room.\n "
                "You must enter a 3 digit code to escape.\n" 
                "Investigate the objects in the room to obtain the 3 digit code.\n")

print(instructions)

#implement objects
def create_objects():
    return [
        GameObject("Sweater", "It's a blue sweater that had the number 12 stitched on it.",
                   "someone has unstitched a second number, leaving only the 1",
                   "the sweater smells of laundry detergent"),
        GameObject("Chair", "It's a wood chair with only 3 legs.",
                   "Someone has snapped off one leg.", "It smells like old wood."),
        GameObject("Journal", "The final entry states that time should be formatted (H-M-S)",
                   "The cover is worn and several pages are missing", "It smells like musty leather."),
        GameObject("Bowel of soup", "It appears to be a bowel of tomato soup",
                   "It has cooled to room temperature", "You detect 7 different herbs and spices"),
        GameObject("Clock", "The hour hand is pointing toward the soup. The minute hand is pointing toward the sweater",
                   "The battery compartment is open and empty", "It smells of plastic")

    ]

mygame = Game(create_objects())
mygame.take_turn()