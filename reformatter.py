import os

def reformat(name):
    os.chdir(r"C:\Users\j0she\Desktop\projects\Drawing Idea Generator")
    original_file = open(name, "r")
    original_file_read = original_file.read()
    original_file.close()
    original_file_read.strip()
    original_file_lines = original_file_read.splitlines()
    formatted_list = []
    for line in original_file_lines:
        if line.isspace() or len(line) <= 1:
            continue
        formatted_list.append(line.lower())

    final_string = ",".join(formatted_list)

    new_file = open(name + "_new", "w")
    new_file.write(final_string)

print("Please enter the name of the list to reformat.")
name = input("> ")
reformat(name)