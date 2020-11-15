import random #allows for random number to be generated


def main_menu():

    #asks for user input
    user_input = input("Would you like to roll the dice? (y/n) ").lower()

    #takes care of invalid user input and asks user for prompt again
    while user_input not in ['y', 'yes', 'no', 'n']:
        user_input = input ("Invalid input. Would you like to roll the dice? (y/n) ")

    #if user says no, program will terminate
    if user_input in ['n', 'no']:
        print("\nTerminating program... Goodbye.")
    else:
        roll_dice () #otherwise, roll the dice


def roll_dice():
    dice = random.randint(1,6) #generates random number from 1-6

#displays appropriate print statement based on number generated
    if dice == 1:
        print("The number rolled is " , dice)
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
            "|         |\n" +
            "|    o    |\n" +
            "|         |\n" +
            "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()

    elif dice ==2:
        print("The number rolled is " , dice)
        #counter=1
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
              "|o        |\n" +
              "|         |\n" +
              "|        o|\n" +
              "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()
    elif dice ==3:
        print("The number rolled is ", dice)
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
              "|o        |\n" +
              "|    o    |\n" +
              "|        o|\n" +
              "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()
    elif dice ==4:
        print("The number rolled is ",dice)
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
              "|o       o|\n" +
              "|         |\n" +
              "|o       o|\n" +
              "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()
    elif dice == 5:
        print("The number rolled is " , dice)
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
              "|o       o|\n" +
              "|    o    |\n" +
              "|o       o|\n" +
              "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()
    else:
        print("The number rolled is " , dice)
        print("\033[9m" +"+ - - - - +\n" + "\033[0m" +
              "|o       o|\n" +
              "|o       o|\n" +
              "|o       o|\n" +
              "\033[9m" +"+ - - - - +\n" + "\033[0m")
        main_menu()

main_menu() #program starts here