from card_maker import make_card, load_cards, save_cards
def main():
    possible_templates = [0,1,2,3,11,12,13,14,20,22,23,24]
    possible_types = [1, 2]

    offdef = False
    department = -1
    skill_levels = [False, False, False, False]
    cost = 0
    description = ""

    print "Welcome to Burn Rate card maker v0.1"
    # Set template
    print "Which template would you like to use? (0-24)"
    template = int(raw_input("Template: "))
    if template not in possible_templates:
        print "Invalid Entry. Using 0."
        template = 0
    
    # Set card type
    print "Please select the type of card that you would like to make."
    print "1. Offensive"
    print "2. Defensive"
    print "Any other entry: Quit"
    offdef = int(raw_input("Choice: "))

    if type not in possible_types:
        print "Goodbye."
        quit()
    else:
        offdef -= 1

    # Set department
    while True:
        print "Which department will this card affect?"
        print "0 = Sales"
        print "1 = Human Resources"
        print "2 = Finance"
        print "3 = Development"
        department = int(raw_input(department))
        if department <= 3 and department >= 0:
            break
        else:
            print "Invalid input"
            continue

    # Set skill levels
    print "Please select which skill levels the card will affect."
    level = 0
    while level <= 3:
        print "Will this card affect level " + str(level) + "?"
        choice = raw_input("(y/n): ")
        if choice == 'y':
            skill_levels[level] = True
        elif choice == 'n':
            level += 1
            continue
        else:
            print "Invalid input
            continue

    # Cost of card
    print "Set the cost of your card. "
    print "For funding, this is the amount ",
    print "of money to add to the player's account."
    print "For a bad idea, this is the amount of engineers/contractors ",
    print "needed to complete the project."
    print "For a Special card, this specifies the amount of VPs needed"
    print "For poach/fire, set the amount of cards this card is worth."
    print "(normally two of the same card are needed to fire one VP; ",
    print "put 1 or press enter if you want to accept the default)"
    print "For all other cards enter 0 or just press enter."
    cost = raw_input("Cost: ")

    try:
        cost = int(cost)
    except ValueError:
        if cost == '':
            if template == 3 or template == 12:
                cost = 1
            else:
                cost = 0

    else:
        cost = int(cost)

    print "Finally, please enter the description for your card."

    description = raw_input("Description: ")

    print "Okay, we are going to make the card. Please confirm below:"
    print "We are going to use template ", template
    print "The card type will be ",

    if offdef:
        print "Offensive"

    else:
        print "Defensive"

    print "The department that this card will affect is ",

    if department == 0:
        print "Sales"
    elif department == 1:
        print "Human Resources"
    elif department == 2:
        print "Finance"
    elif department == 3:
        print "Development"
    else:
        print "Other/Error. Please quit me now."

    print "The skill levels that this card will affect are ",

    for i in range(len(skill_levels)):
        if skill_levels[i]:
            print i,
            print " ",

    print

    print "The cost of the card will be ", cost
    print "The description of the card will be"
    print description
    print
    print "Make the card?"
    make = raw_input("(Y/n): ")

    if make == "y" or make == "Y" or make == "":
        location = raw_input("Location of cards (default cards.xml): ")
        if not location:
            location = "cards.xml"
        try:
            card_deck = load_cards(location)
        except IOError:
            pass
        makecard(card_deck, offdef, department, skill_levels, cost,
                 description, template)
    else:
        print "Cancelled. ",

    print "Quitting..."
    

if __name__ == "__main__":
    main()
