def save_card(location):
    pass

def make_card(offdef, department, skill_levels, cost, description, template=0):
    pass

def main():
    possible_types = [1, 2]

    offdef
    department = -1
    skill_levels = [False, False, False, False]
    cost = 0
    description = ""

    # Set card type
    print "Welcome to Burn Rate card maker v0.1"
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

    

if __name__ == "__main__":
    main()
