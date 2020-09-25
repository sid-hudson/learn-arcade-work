import random
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")
    done = False
    miles_traveled = 0
    thirst = 0
    canteen = 3
    camel_tiredness = 0
    native_travel = -20
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print(" ")
        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            done = True
            print("Thanks for playing!")

        elif user_choice.upper() == "A":
            if canteen >= 1:
                canteen -= 1
                thirst = 0

            elif canteen == 1:
                print("error")

        elif user_choice.upper() == "B":
            miles_traveled += random.randrange(5, 13)
            print("You traveled")
            thirst += 1
            camel_tiredness += 1
            native_travel += random.randrange(7, 15)

        elif user_choice.upper() == "C":
            miles_traveled += random.randrange(10, 21)
            print("You traveled")
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            native_travel += random.randrange(7, 15)

        elif user_choice.upper() == "D":
            print("Your camel is happy.")
            camel_tiredness = 0
            native_travel += random.randrange(7, 15)

        elif user_choice.upper() == "E":
            print("Miles traveled:  ", miles_traveled)
            print("Drinks in canteen:  ", canteen)
            print("The natives are ", miles_traveled - native_travel, " miles behind you.")

        if thirst > 4:
            print("You are thirsty")

        elif thirst > 6:
            print("You died of thirst!")
            done = True

        if camel_tiredness > 5:
            print("Your camel is tired")

        elif camel_tiredness > 8:
            print("Your camel is dead!")
            done = True

        if native_travel == miles_traveled:
            print("The natives have caught you!")
            done = True

        elif native_travel < 15:
            print("The natives are getting close!")

        if miles_traveled > 200:
            print("You won!")
            done = True

        for i in range(20):
            if random.randrange(5) == 0:
                print("You have found an oasis!")


main()