import random
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")
    done = False
    miles_traveled = 0
    thirst = 3
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

        elif user_choice.upper() == "D":
            print("Your camel is happy.")
            camel_tiredness = 0

        elif user_choice.upper() == "E":
            print("Miles traveled:  ", miles_traveled)
            print("Drinks in canteen:  ", thirst)
            print("The natives are ", native_travel, " miles behind you.")


main()