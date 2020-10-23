import random
import os

welcome_text = "Welcome to Drawing Idea Generator!"
os.chdir(r"./option_files")
mode = 'R'


def start():
    global mode
    print(welcome_text)
    mode = choose_mode()
    find_idea()
    

def find_idea():
    end = False
    chosen_element = None
    while end != True:
        if chosen_element == None:
            chosen_element = choose_element("categories")
        if chosen_element[0] == "_":
            chosen_element = choose_element(chosen_element, True)
            print
            end = True
        else:
            chosen_element = choose_element(chosen_element)
    restart = input("Would you like to choose again? (If so, enter 'Y')")
    if restart.capitalize() == "Y":
        start()
    

def choose_element(name, end = False):
    options_file = open(name, "r")
    options = options_file.read().split(",")
    options_file.close()

    random_elements = []
    if mode == 'R':
        number_of_options = int(min(max(3, len(options)/3), 8))
    else:
        number_of_options = int(len(options))

    for i in range(number_of_options):
        random_element = options.pop(random.randint(0, len(options) - 1))
        random_elements.append(random_element)
        print(str(i) + ": " + random_element.strip("_").capitalize())
    
    if end == True:
        print("^^ Please choose an idea from the above ^^")
    else:
        print("^^ Please choose a category from the above ^^")

    input_valid = False
    while input_valid != True:
        chosen_index = input("> ")
        if chosen_index.isdigit():
            if int(chosen_index) <= (len(random_elements) - 1) and int(chosen_index) >= 0:
                input_valid = True
                break
        print("Sorry, that option isn't valid, please try again.")
    
    chosen_element = random_elements[int(chosen_index)]
    print("You chose: " + str(chosen_element).strip("_").upper() + ".")
    return chosen_element


def choose_mode():
    input_valid = False
    while input_valid != True:
        mode = input("Please choose either Random (R) or Catalogue (C) mode.")
        try:
            mode = mode.capitalize()
            if mode == 'R' or mode == 'C':
                return mode
            print("Sorry, that option isn't valid, please try again.")
        except:
            print("Sorry, that option isn't valid, please try again.")

start()