import random
def main():
    print("Welcome to Waterdeep!")
    print("You have escaped from an orc camp with some stolen horses and are now on your way back to Waterdeep.")
    print("The orcs won't let you escape them so easily though and are now chasing you across the Sword Coast!")
    print("Survive your journey along the coast and mae it to Waterdeep!")
    print(" ")
    done = False
    miles_traveled = 0
    thirst = 0
    canteen = 3
    horse_tiredness = 0
    orc_travel = -20
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print("")
        user_choice = input("What is your choice? ")

        # Quit
        if user_choice.upper() == "Q":
            done = True
            print("Thanks for playing Waterdeep!")

        # Drink from canteen
        elif user_choice.upper() == "A":
            if canteen >= 1:
                canteen -= 1
                thirst = 0
            elif canteen == 1:
                print("error")

        # Go moderate speed
        elif user_choice.upper() == "B":
            new_miles_moderate = random.randrange(5, 13)
            miles_traveled += new_miles_moderate
            print("You traveled", new_miles_moderate, "miles.")
            thirst += 1
            horse_tiredness += 1
            orc_travel += random.randrange(7, 15)
            if random.randrange(20) == 0:
                print("You have came upon a hidden elf camp!")
                print("They have decided to help you buy refilling your canteen and feeding your horse!")
                canteen = 3
                horse_tiredness = 0
                thirst = 0
                print("Your canteen is full and your horse is now happy.")

        # Go full speed
        elif user_choice.upper() == "C":
            new_miles_speed = random.randrange(10, 21)
            miles_traveled += new_miles_speed
            print("You traveled", new_miles_speed, "miles.")
            thirst += 1
            horse_tiredness += random.randrange(1, 4)
            orc_travel += random.randrange(7, 15)
            for i in range(100):
                if random.randrange(100) == 0:
                    print("You have came upon a hidden elf camp!")
                    print("They have decided to help you buy refilling your canteen and feeding your horse!")
                    canteen = 3
                    horse_tiredness = 0
                    thirst = 0
                    print("Your canteen is full and your horse is now happy.")

        # Rest for the night
        elif user_choice.upper() == "D":
            print("Your horse is happy.")
            horse_tiredness = 0
            orc_travel += random.randrange(7, 15)

        # Status check
        elif user_choice.upper() == "E":
            print("Miles traveled:  ", miles_traveled)
            print("Drinks in canteen:  ", canteen)
            print("The orcs are ", miles_traveled - orc_travel, " miles behind you.")

        if thirst >= 4:
            print("You are thirsty")

        elif thirst >= 6:
            print("You died of thirst!")
            done = True

        if horse_tiredness >= 5:
            print("Your horse is tired")

        elif horse_tiredness >= 8:
            print("Your horse is dead!")
            done = True

        if orc_travel >= miles_traveled:
            print("The orcs have caught you!")
            done = True

        elif orc_travel <= 15:
            print("The orcs are getting close!")

        if not done and miles_traveled > 200:
            print("You have made it to Waterdeep and you have escaped the orcs!")
            done = True

main()