class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class Item:
    def __init__(self, room_number, long_description, short_name):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name


def main():

    # Room numbers 0-5
    room_list = []
    cell_room = Room("You are in a dark cell, there is a pile of bones laying in the center of the room."
                     "there also seems to be a key laying in the corner of the room."
                     "There is one locked door to the south of the room.", None, 1, None, None)
    room_list.append(cell_room)

    dungeon_room = Room("You are now in what seems to look like the dungeon room."
                        "There is a desk in the center of the room. The desk has two drawers that are locked."
                        "On top of the desk there is a bronze key and a silver key."
                        "There is a door to the north of the room and stairs that lead up to a door east of the room.",
                        0, None, 2, None)
    room_list.append(dungeon_room)

    hallway = Room("You are now in the hallway. There are three doorways, one to the west of the room,"
                   "one door leads north of the room, and the other door is on the east side of the room."
                   "There is also a bookcase in the room and in front of that bookcase there is a small table."
                   "On top of that table is a locked chest with three key holes.", 5, None, 3, 1)
    room_list.append(hallway)

    dinning_room = Room("You have entered the dinning room."
                        "In ths room there is a large dinning table that holds three dishes."
                        "One dish has a nice steak sitting on it, the other is a pie that still looks like it's warm."
                        "The other is just a simpled jug of water. There are two doors in this room."
                        "One door is one the North side of the room while the door leads to the west.",
                        4, None, None, 2)
    room_list.append(dinning_room)

    kitchen = Room("You have now entered the kitchen. There are two doors in this room."
                   "One is on the South side of the room and the other door leads to the West."
                   "There is also a cupboard that seems to be locked as well as a knife that is sitting on the counter."
                   , None, 3, None, 5)
    room_list.append(kitchen)

    great_hall = Room("You have now entered the great hall. Inside this room is a vicious dog who looks like"
                      "he's going to attack! Also in this room there are three doors."
                      "One door is on the south side of the room, another is on the east side. The last door is locked."
                      "It seems that it might lead outside!", None, 2, 4, None)
    room_list.append(great_hall)

    item_list = []
    key = Item(0, "A rusty metal key. It must unlock something.", "key")
    item_list.append(key)

    bone = Item(0, "A human bone. Gross, why would you pick that up.", "bone")
    item_list.append(bone)

    bronze_key = Item(1, "A small bronze key. It must unlock something.", "bronze key")
    item_list.append(bronze_key)

    silver_key = Item(1, "A small silver key. It must unlock something.", "silver key")
    item_list.append(silver_key)

    gold_key = Item(1, "A small gold key. It must unlock something.", "gold key")
    item_list.append(gold_key)

    green_key = Item(1, "A small key with green tape on it. It must unlock something.", "green key")
    item_list.append(green_key)

    desk = Item(1, "A desk with two locked drawers.", "desk")
    item_list.append(desk)

    chest = Item(2, "A small chest with three key holes.", "chest")
    item_list.append(chest)

    diamond_key = Item(2, "A small key encrusted with diamonds. It must unlock something.", "diamond key")
    item_list.append(diamond_key)

    book_case = Item(2, "A large book case that holds several books and newspapers.", "book case")
    item_list.append(book_case)

    steak = Item(3, "A delicious steak.", "steak")
    item_list.append(steak)

    pie = Item(3, "A nice warm pie.", "pie")
    item_list.append(pie)

    blue_key = Item(3, "A small key with blue tape on it.", "blue key")
    item_list.append(blue_key)

    water = Item(3, "A nice tall jug of water, you must be thirsty.", "water")
    item_list.append(water)

    cupboard = Item(4, "A locked cabinet. I wonder whats inside.", "cupboard")
    item_list.append(cupboard)

    black_key = Item(4, "A small key with black tape on it. It must open something.", "black key")
    item_list.append(black_key)

    knife = Item(4, "A sharp kitchen knife. Be careful not to hurt yourself.", "knife")
    item_list.append(knife)

    dog = Item(5, "A vicious dog, he looks like he might attack.", "dog")
    item_list.append(dog)

    door = Item(5, "A locked door, it might lead outside.", "door")
    item_list.append(door)

    current_room = 0
    done = False
    while not done:
        print(room_list[current_room].description)
        print()
        room_choice = input("Where do you want to go? ")
        if room_choice.upper() == "NORTH" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif room_choice.upper() == "SOUTH" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif room_choice.upper() == "EAST" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif room_choice.upper() == "WEST" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print("Not this way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "QUIT" or room_choice.upper() == "Q":
            done = True
            print("Thank you for playing!")
            print()
        else:
            print("I don't understand.")
            print()


main()