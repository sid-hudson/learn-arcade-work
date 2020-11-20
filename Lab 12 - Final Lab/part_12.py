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
    cell_room = Room("You are in a dark damp cell.\n"
                     "There is one locked door to the south of the room.", None, 1, None, None)
    room_list.append(cell_room)

    dungeon_room = Room("You are now in what seems to look like the dungeon room.\n"
                        "There is a desk in the center of the room. The desk has two drawers that are locked.\n"
                        "There is a door to the north of the room and stairs that lead up to a door east of the room.",
                        0, None, 2, None)
    room_list.append(dungeon_room)

    hallway = Room("You are now in the hallway. There are three doorways, one to the west of the room,\n"
                   "one door leads north of the room, and the other door is on the east side of the room.\n"
                   "There is also a bookcase in the room and in front of that bookcase there is a small table."
                   , 5, None, 3, 1)
    room_list.append(hallway)

    dinning_room = Room("You have entered the dinning room.\n"
                        "In ths room there is a large dinning table.\n"
                        "There are two doors in this room.\n"
                        "One door is one the North side of the room while the door leads to the west.",
                        4, None, None, 2)
    room_list.append(dinning_room)

    kitchen = Room("You have now entered the kitchen. There are two doors in this room.\n"
                   "One is on the South side of the room and the other door leads to the West.\n"
                   "There is also a cupboard that seems to be locked."
                   , None, 3, None, 5)
    room_list.append(kitchen)

    great_hall = Room("You have now entered the great hall. Inside this room is a vicious dog who looks like\n"
                      "he's going to attack! Also in this room there are three doors.\n"
                      "One door is on the south side of the room, another is on the east side.\n"
                      "The last door is locked, it seems that it might lead outside!", None, 2, 4, None)
    room_list.append(great_hall)

    # Item List
    item_list = []
    key = Item(0, "A there is a rusty metal key laying on the floor.", "key")
    item_list.append(key)

    bone = Item(0, "There is a pile of bones scattered on the floor.", "bone")
    item_list.append(bone)

    bronze_key = Item(1, "There is a small bronze key laying on the desk.", "bronze key")
    item_list.append(bronze_key)

    silver_key = Item(1, "There is silver key laying on the desk.", "silver key")
    item_list.append(silver_key)

    gold_key = Item(-1, "Inside the drawer there is a golden key.", "gold key")
    item_list.append(gold_key)

    green_key = Item(-1, "Inside the drawer there is a small key with green tape on it.", "green key")
    item_list.append(green_key)

    chest = Item(2, "On top of the table there is a small chest with three key holes", "chest")
    item_list.append(chest)

    diamond_key = Item(-1, "Inside the chest there is a diamond encrusted key", "diamond key")
    item_list.append(diamond_key)

    steak = Item(3, "One the dinning table there is a nice juicy steak.", "steak")
    item_list.append(steak)

    pie = Item(3, "There is also a nice warm pie on the dinning table.", "pie")
    item_list.append(pie)

    blue_key = Item(-1, "Inside the pie there is a key with blue tape on it.", "blue key")
    item_list.append(blue_key)

    water = Item(3, "Also on the table there is a jug of cold water.", "water")
    item_list.append(water)

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
        # print room description
        print()
        print(room_list[current_room].description)

        # print items in room
        for item in item_list:
            if item.room_number == current_room:
                print(item.long_description)
        print()

        # get user input
        user_choice = input("What would you like to do?")
        user_words = user_choice.split(" ")
        if len(user_words) > 1 and user_words[1].upper() == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("Not this way.")
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("Not this way.")
                print()
            else:
                current_room = next_room

        # Get command
        elif user_words[0].upper() == "GET":
            success = False
            for item in item_list:
                if user_words[1].lower() == item.short_name and item.room_number == current_room:
                    item.room_number = -2
                    print(f"You have picked up {item.short_name}.")
                    success = True
            if not success:
                print("You can't do that")

        # Inventory command
        elif user_words[0].upper() == "INVENTORY":
            for item in item_list:
                if item.room_number == -2:
                    print(item.short_name)

        # Drop command
        elif user_words[0].upper() == "DROP":
            success = False
            for item in item_list:
                if user_words[1].lower() == item.short_name and item.room_number == -1:
                    item.room_number = current_room
                    print(f"You have dropped {item.short_name}.")
                    success = True
            if not success:
                print("You can't do that.")

        # use command
        elif user_words[0].upper() == "USE":
            for item in item_list:
                if item.room_number == -2:
                    if item.short_name.lower() == "steak" and current_room == 5:
                        print("The dog is happy.")
                        item.room_number = -1
                    elif item.short_name.lower() == "knife" and current_room == 5:
                        print("The dog is dead")
                        item.room_number = -1
                    elif item.short_name.lower() == "bone" and current_room == 5:
                        print("The dog is happy")
                        item.room_number = -1
                    elif item.short_name.lower() == "key" and current_room == 0:
                        print("The door is now unlocked.")
                        item.room_number = -1
                    elif item.short_name.lower() == "bones" and current_room == 5:
                        print("The dog is happy.")
                        item.room_number = -1
                    elif item.short_name.lower() == "bronze key" and current_room == 1:
                        print("You opened one of the drawers")
                        bronze_key.room_number = 1
                        item.room_number = -1
                    elif item.short_name.lower() == "blue key" and current_room == 1:
                        print("You have opened one of the drawers.")
                        green_key.room_number = 1
                        item.room_number = -1
                    # Chest commands
                    elif item.short_name.lower() == "silver key" and current_room == 2:
                        print("The chest unlocks slightly.")
                        item.room_number = -1
                    elif item.short_name.lower() == "green key" and current_room == 2:
                        print("The chest unlocks slightly.")
                        item.room_number = -1
                    elif item.short_name.lower() == "black key" and current_room == 2:
                        print("The chest unlocks slightly.")
                        item.room_number = -1
                    elif item.short_name.lower() == "book case" and current_room == 2:
                        print("You find a newspapers, the headline reads 'TOWN WATER SUPPLY POISONED!'")
                        item.room_number = -1
                    elif item.short_name.lower() == "pie" and current_room == 3:
                        print("Theres something in the pie!")
                        blue_key.room_number = 3
                        item.room_number = -1
                    elif item.short_name.lower() == "water" and current_room == 3:
                        done = True
                        print("The water was poisoned, you have died. Thank you for playing!")
                    elif item.short_name.lower() == "gold key" and current_room == 4:
                        print("You have opened the cupboard.")
                        black_key.room_number = 4
                        item.room_number = -1
                    elif item.short_name.lower() == "diamond key" and current_room == 5:
                        "You have unlocked the door and escaped the mansion. Congratulations!"
                        done = True
                    else:
                        print("You can't do that.")

        elif user_choice.upper() == "QUIT":
            done = True
            print("Thank you for playing!")
            print()
        else:
            print("I don't understand.")
            print()


main()
