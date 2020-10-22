import random
import os

welcome_text = "Welcome to Drawing Idea Generator!😃😃"
#print("Current working directory is: "+os.getcwd())
os.chdir(r"./option_files")

def start():
    print(welcome_text)
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
        print(welcome_text)
        find_idea()
    
def choose_element(name, end = False):
    if end == True:
        print("Please choose an idea from the below:")
    else:
        print("Please choose a category from the below:")
    options_file = open(name, "r")
    options = options_file.read().split(",")
    options_file.close()

    random_elements = []
    number_of_options = int(min(max(3, len(options)/3), 8))

    for i in range(number_of_options):
        random_element = options.pop(random.randint(0, len(options) - 1))
        random_elements.append(random_element)
        print(str(i) + ": " + random_element.strip("_").capitalize())
    
    chosen_index = int(input("> "))
    chosen_element = random_elements[chosen_index]
    print("You chose: " + str(chosen_element).strip("_").upper() + ".")
    return chosen_element

start()