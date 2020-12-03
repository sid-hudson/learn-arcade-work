import random


class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class Item:
    def __init__(self, room_number, long_description, short_name, weapon_damage = 0):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name
        self.weapon_damage = weapon_damage


class User:
    def __init__(self, max_hit_points, current_hit_points):
        self.max_hit_points = 10
        self.current_hit_points = 10


class Enemy:
    def __init__(self, room_number, long_description, short_name, max_hit_points, current_hit_points, enemy_damage):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points
        self.enemy_damage = enemy_damage


def main():

    silver_lock = False
    green_lock = False
    black_lock = False
    bronze_lock = False
    blue_lock = False

    user = User(10, 10)

    # Room numbers 0-5
    room_list = []
    cell_room = Room("You are in a dark damp cell.\n"
                     "There is one door on the south side of the room, it is currently locked.", None, None, None, None)
    room_list.append(cell_room)

    dungeon_room = Room("You are in what seems a dungeon room.\n"
                        "There is a desk in the center of the room. The desk has two drawers that are locked.\n"
                        "There is a door to the north of the room and stairs that lead up to a door east of the room.",
                        0, None, 2, None)
    room_list.append(dungeon_room)

    hallway = Room("You are in the hallway. There are three doorways, one on the west side of the room,\n"
                   "one door leads north of the room, and the other door is on the east side of the room."
                   , 5, None, 3, 1)
    room_list.append(hallway)

    dinning_room = Room("You are in the dinning room.\n"
                        "In ths room there is a large dinning table.\n"
                        "There are two doors in this room.\n"
                        "One door is one the North side of the room while the other door leads to the west.",
                        4, None, None, 2)
    room_list.append(dinning_room)

    kitchen = Room("You are in the kitchen. There are two doors in this room.\n"
                   "One is on the South side of the room and the other door leads to the West.\n"
                   "There is also a cupboard that seems to be locked."
                   , None, 3, None, 5)
    room_list.append(kitchen)

    great_hall = Room("You are in the great hall. In this room there are three door ways.\n"
                      "One door is on the south side of the room, another is on the east side.\n"
                      "The last door is locked, it seems that it might lead outside!", None, 2, 4, None)
    room_list.append(great_hall)

    # Item List
    item_list = []
    key = Item(0, "There is a rusty metal key laying on the floor.", "key")
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

    bookcase = Item(2, "There is also bookcase filled with books and newspapers. \n"
                       "In front of the bookcase is a small table with a chest on it. \n"
                       "This chest has three locks on it: a silver lock, a green lock, and a black lock."
                       , "bookcase")
    item_list.append(bookcase)

    diamond_key = Item(-1, "Inside the chest there is a diamond encrusted key", "diamond key")
    item_list.append(diamond_key)

    steak = Item(3, "On the dinning table there is a nice juicy steak.", "steak")
    item_list.append(steak)

    pie = Item(3, "There is also a nice warm pie on the table.", "pie")
    item_list.append(pie)

    blue_key = Item(-1, "Inside the pie there is a key with blue tape on it.", "blue key")
    item_list.append(blue_key)

    water = Item(3, "Also on the table there is a jug of nice refreshing water.", "water")
    item_list.append(water)

    black_key = Item(4, "Inside the cupboard is a key with black tape on it.", "black key")
    item_list.append(black_key)

    knife = Item(4, "on the counter there is a sharp knife.", "knife", random.randrange(3, 7))
    item_list.append(knife)

    dog = Enemy(5, "There is a  vicious dog in the room, he looks like he might attack!", "dog",
                10, 10, random.randrange(3, 5))
    item_list.append(dog)

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
        user_choice = input("What would you like to do? ")
        user_words = user_choice.split(" ")

        # Get direction
        if len(user_words) > 2:
            user_words[1] = user_words[1] + " " + user_words[2]

        if len(user_words) > 1 and user_words[1].upper() == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You cannot go this way.")
                print()
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You cannot go this way.")
                print()
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You cannot go this way.")
                print()
            else:
                current_room = next_room

        elif len(user_words) > 1 and user_words[1].upper() == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You cannot go this way.")
                print()
            else:
                current_room = next_room

        # Get command
        elif user_words[0].upper() == "GET":
            success = False

            # Item get command
            for item in item_list:
                if user_words[1].lower() == item.short_name and item.room_number == current_room:
                    item.room_number = -2
                    print(f"You have picked up the {item.short_name}.")
                    success = True

            if not success:
                print("You can't do that")

        # Inventory command
        elif user_words[0].upper() == "INVENTORY":

            # Item inventory
            for item in item_list:
                if item.room_number == -2:
                    print("Inventory:")
                    print(item.short_name)

        # Drop command
        elif user_words[0].upper() == "DROP":
            success = False

            # Item drop command
            for item in item_list:
                if user_words[1].lower() == item.short_name and item.room_number == -1:
                    item.room_number = current_room
                    print(f"You have dropped the {item.short_name}.")
                    success = True

            if not success:
                print("You can't do that.")

        # use command
        elif user_words[0].upper() == "USE":
            if len(user_words) == 1:
                print("What do you want to use? ")
                continue

            # Item use command in room
            if item.room_number == current_room:
                if item.short_name.lower() == "bookcase" and current_room == 2:
                    print("You find a newspapers, the headline reads 'TOWN WATER SUPPLY POISONED!'")
                    continue

                elif item.short_name.lower() == "pie" and current_room == 3:
                    print("Theres something in the pie!")
                    blue_key.room_number = 3
                    item.room_number = -1
                    continue

                elif item.short_name.lower() == "water" and current_room == 3:
                    done = True
                    print("The water was poisoned, you have died. Thank you for playing!")
                    continue

            has_item = False

            # Item use command
            for item in item_list:
                if item.room_number == -2 and user_words[1].lower() == item.short_name:
                    has_item = True
                    break
            if not has_item:
                print("You don't have that.")
                continue

            if item.short_name.lower() == "steak" and current_room == 5:
                print("You fed the steak to the dog, he is now happy!")
                item.room_number = -1
                dog.room_number = -1
            elif item.short_name.lower() == "bone" and current_room == 5:
                print("You gave the dog a bone and he is now happy!")
                item.room_number = -1
                dog.room_number = -1
            elif item.short_name.lower() == "key" and current_room == 0:
                print("The door is now unlocked.")
                item.room_number = -1
                room_list[0].south = 1
                room_list[0].description = "You are in a dark damp cell.\n" +\
                                           "There is one door on the south side of the room."
            elif item.short_name.lower() == "bronze key" and current_room == 1:
                print("You opened one of the drawers")
                gold_key.room_number = 1
                item.room_number = -1
                bronze_lock = True
                room_list[1].description = "You are in what seems to be a dungeon room.\n" +\
                                           "There is a desk in the center of the room. " \
                                           "The desk has one drawer that is locked.\n" +\
                                           "There is a door to the north of the room and stairs " \
                                           "that lead up to a door east of the room."
            elif item.short_name.lower() == "blue key" and current_room == 1:
                print("You have opened one of the drawers.")
                green_key.room_number = 1
                item.room_number = -1
                blue_lock = True
                room_list[1].description = "You are in what seems to be a dungeon room.\n" + \
                                           "There is a desk in the center of the room. " \
                                           "The desk has one drawer that is locked.\n" + \
                                           "There is a door to the north of the room and stairs " \
                                           "that lead up to a door east of the room."
            elif bronze_lock == True and blue_lock == True:
                room_list[1].description = "You are in what seems to be a dungeon room.\n" + \
                                           "There is a desk in the center of the room. \n" + \
                                           "There is a door to the north of the room and stairs " \
                                           "that lead up to a door east of the room."

            # Chest commands
            elif item.short_name.lower() == "silver key" and current_room == 2:
                silver_lock = True
                item.room_number = -1
                print("You unlocked the silver lock!")

            elif item.short_name.lower() == "green key" and current_room == 2:
                green_lock = True
                item.room_number = -1
                print("You have unlocked the green lock!")

            elif item.short_name.lower() == "black key" and current_room == 2:
                black_lock = True
                item.room_number = -1
                print("You unlocked the black lock!")

            elif silver_lock == True and green_lock == True and black_lock == True:
                diamond_key.room_number = 2
                print("You unlocked the chest!")

            elif item.short_name.lower() == "gold key" and current_room == 4:
                print("You opened the cupboard.")
                black_key.room_number = 4
                item.room_number = -1
                room_list[4].description = "You are in the kitchen. There are two doors in this room.\n" +\
                                           "One is on the South side of the room and " \
                                           "the other door leads to the West.\n" +\
                                           "There is also a cupboard."

            elif item.short_name.lower() == "diamond key" and current_room == 5:
                "You have unlocked the door and escaped the mansion. Congratulations!"
                done = True

            elif item.short_name.lower() == "knife" and current_room == 5 and dog.room_number == current_room:
                weapon_damage = random.randrange(5, 9)
                dog.current_hit_points -= weapon_damage
                print(f"You have done {weapon_damage} damage to the dog.")

                if dog.current_hit_points <= 5:
                    print("The dog looks hurt.")

                elif dog.current_hit_points <= 0:
                    print("dog is dead")
                    dog.room_number = -1

            else:
                print("You can't do that.")

        elif user_choice.upper() == "QUIT":
            done = True
            print("Thank you for playing!")
            print()
        else:
            print("I don't understand.")
            print()

        if current_room == 5 and dog.room_number == current_room:
            enemy_damage = random.randrange(2, 6)
            user.current_hit_points -= enemy_damage
            print(f"The dog attacks you. They have done {enemy_damage} damage. "
                  f"You have {user.current_hit_points} health left.")
            if user.current_hit_points <= 0:
                done = True
                print("The dog has killed you. Thank you for playing!")


main()
