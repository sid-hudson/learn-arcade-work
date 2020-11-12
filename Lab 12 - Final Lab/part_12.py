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
    cell_room = Room(" \n"
                     "You are in a dark damp cell. \n"
                     "There is one locked door to the south of the room.", None, 1, None, None)
    room_list.append(cell_room)

    dungeon_room = Room(" \n"
                        "You are now in what seems to look like the dungeon room.\n"
                        "There is a desk in the center of the room. The desk has two drawers that are locked.\n"
                        "There is a door to the north of the room and stairs that lead up to a door east of the room.",
                        0, None, 2, None)
    room_list.append(dungeon_room)

    hallway = Room(" \n"
                   "You are now in the hallway. There are three doorways, one to the west of the room,\n"
                   "one door leads north of the room, and the other door is on the east side of the room.\n"
                   "There is also a bookcase in the room and in front of that bookcase there is a small table."
                   , 5, None, 3, 1)
    room_list.append(hallway)

    dinning_room = Room(" \n"
                        "You have entered the dinning room.\n"
                        "In ths room there is a large dinning table.\n"
                        "There are two doors in this room.\n"
                        "One door is one the North side of the room while the door leads to the west.",
                        4, None, None, 2)
    room_list.append(dinning_room)

    kitchen = Room(" \n"
                   "You have now entered the kitchen. There are two doors in this room.\n"
                   "One is on the South side of the room and the other door leads to the West.\n"
                   "There is also a cupboard that seems to be locked."
                   , None, 3, None, 5)
    room_list.append(kitchen)

    great_hall = Room(" \n"
                      "You have now entered the great hall. Inside this room is a vicious dog who looks like\n"
                      "he's going to attack! Also in this room there are three doors.\n"
                      "One door is on the south side of the room, another is on the east side.\n"
                      "The last door is locked, it seems that it might lead outside!", None, 2, 4, None)
    room_list.append(great_hall)

    item_list = []
    key = Item(0, "A there is a rusty metal key laying on the floor.", "key")
    item_list.append(key)

    bone = Item(0, "There is a pile of bones scattered on the floor.", "bone")
    item_list.append(bone)

    cell_door = Item(0, "A cell door that is locked.", "cell door")
    item_list.append(cell_door)

    bronze_key = Item(1, "There is a small bronze key laying on the desk.", "bronze key")
    item_list.append(bronze_key)

    silver_key = Item(1, "There is silver key laying on the desk.", "silver key")
    item_list.append(silver_key)

    gold_key = Item(-1, "Inside the drawer there is a golden key.", "gold key")
    item_list.append(gold_key)

    green_key = Item(-1, "Inside the drawer there is a small key with green tape on it.", "green key")
    item_list.append(green_key)

    desk = Item(1, "A desk with two locked drawers.", "desk")
    item_list.append(desk)

    chest = Item(2, "A small chest with three key holes.", "chest")
    item_list.append(chest)

    diamond_key = Item(-1, "Inside the chest there is a diamond encrusted key", "diamond key")
    item_list.append(diamond_key)

    book_case = Item(2, "A large book case that holds several books and newspapers.", "book case")
    item_list.append(book_case)

    steak = Item(3, "One the dinning table there is a nice juicy steak.", "steak")
    item_list.append(steak)

    pie = Item(3, "There is also a nice warm pie on the dinning table.", "pie")
    item_list.append(pie)

    blue_key = Item(-1, "Inside the pie there is a key with blue tape on it.", "blue key")
    item_list.append(blue_key)

    water = Item(3, "Also on the table there is a jug of cold water.", "water")
    item_list.append(water)

    cupboard = Item(4, "A locked cabinet. I wonder whats inside.", "cupboard")
    item_list.append(cupboard)

    black_key = Item(4, "Inside the cupboard is a key with black tape on it.", "black key")
    item_list.append(black_key)

    knife = Item(4, "On the counter there is a sharp knife.", "knife")
    item_list.append(knife)

    dog = Item(5, "A vicious dog, he looks like he might attack.", "dog")
    item_list.append(dog)

    door = Item(5, "A locked door, it might lead outside.", "door")
    item_list.append(door)

    current_room = 0
    done = False
    while not done:
        print(room_list[current_room].description)
        for item in item_list:
            if item.room_number == current_room:
                print(item.long_description)
        print()
        user_choice = input("What would you like to do?")
        if user_choice.upper() == "GO NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "GO SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "GO EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif user_choice.upper() == "GO WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("Not this way.")
                print()
            else:
                current_room = next_room

        elif user_choice.upper() == "QUIT":
            done = True
            print("Thank you for playing!")
            print()
        else:
            print("I don't understand.")
            print()


main()
