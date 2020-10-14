class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():

    # Room numbers 0-5
    room_list = []
    room = Room("You are in a cell. There is an open door to the south.", None, 1, None, None)
    room_list.append(room)

    room = Room("You are in the dungeon room. There is a door to the north, "
                "and stairs leading to a door on the west side of the room.", 0, None, 2, None)
    room_list.append(room)

    room = Room("You are in a hall. There are three doors. The one you entered the rooms in leads to the west. "
                "One door leads north, and the other is on the east side of the room.", 5, None, 3, 1)
    room_list.append(room)

    room = Room("You are in the dinning room. There is a door on the north side of the room, "
                "and one on the west side.", 4, None, None, 2)
    room_list.append(room)

    room = Room("You are in the kitchen. There is a door on the west side of the room, "
                "and another door on the south side of the room.", None, 3, None, 5)
    room_list.append(room)

    room = Room("You are in the main hall. There are three doors. "
                "One door is on the north side of the room and seems to lead outside. "
                "A second door is located on the south side of the room, "
                "and the last door is located on the east side of the room.", None, 2, None, 4)
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print(room_list[current_room].description)
        print()
        user_input = input("Where do you want to go?")
        room_choice = user_input
    if room_choice.upper() == "North" or room_choice.upper() == "N":
        next_room = room_list[current_room].north
    if next_room is None:
        print("Not this way.")
    else:
        current_room = next_room

    if room_choice.upper() == "South" or room_choice.upper() == "S":
        next_room = room_list[current_room].south
    if next_room is None:
        print("Not this way.")
    else:
        current_room = next_room

    if room_choice.upper() == "East" or room_choice.upper() == "E":
        next_room = room_list[current_room].east
    if next_room is None:
        print("Not this way.")
    else:
        current_room = next_room

    if room_choice.upper() == "West" or room_choice.upper() == "W":
        next_room = room_list[current_room].west
    if next_room is None:
        print("Not this way.")
    else:
        current_room = next_room

    if room_choice.upper() == "Quit" or room_choice.upper() == "Q":
        done = True
        print("Thank you for playing!")
    else:
        print("I don't understand.")
main()