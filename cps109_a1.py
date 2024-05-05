# Michelle Nguyen
# CPS109
# Elodie Lugez - Section 4
# 24/11/23

'''
PROBLEM DESCRIPTION

I often make small mistakes in calculating values for physics, and cannot neatly keep track of my data.

Objective of the program is to calculate scalar values from physics equations and
save the values in a .txt file (physics_data.txt) for the user to access.
There will be a main menu for the user to decide if they want to
calculate values, add a new value to physics_data.txt or read physics_data.txt.

If the user wishes to calculate a value, they will be prompted for variable input required for the desired equation.
If the user wishes to add a new value to physics_data.txt, they will be prompted for a variable name and the value.
If the user wishes to read physics_data.txt, the program will open the file and read it.

Program has three main features:
1. Calculate values for physics equations
2. Store values (physics data) in a .txt file
3. Read values (physics data) from the .txt file and output to user

Side feature (implemented for grading purposes):
4. Store the user's interaction with the text GUI in a separate .txt file, essentially an output log
'''


# -------------------------------------------
# START OF FUNCTIONS
# -------------------------------------------

def space():
    '''
    Puts spaces in between blocks of output text
    '''
    print("\n"*2)


def validate(choice, options):
    '''
    Confirms if the user selected a valid option
    
    choice is user input of desired option
    options is a list of acceptable options
    
    Return True if user entered a choice within the list of options
    Return False otherwise
    '''
    if choice in options:
        return True
    else:
        print("That was not a valid option, please enter again.")
        program_output("That was not a valid option, please enter again.")
        return False


# -------------------------------------------
# FILES
# -------------------------------------------

def program_output(s):
    '''
    Writes to output file, cps109_a1_output.txt
    
    Takes str or list as input for s
    
    If s is a str, append to output file
    If s is a list, separate each element into a new line in output file
    '''
    
    # Try to open the output file
    try:
        p = open("cps109_a1_output.txt", "a")
        
        # If the given s is a string, append to output file
        if type(s) == str:
            p.write(s + "\n")
            p.write("\n"*3)
        
        # If the given s is a list, append each element in the list to the output file
        if type(s) == list:
            p.writelines(line + "\n" for line in s)
            p.write("\n"*3)
        
        p.close()
    
    except:
        print("Program output not successfully written.")
    

def open_data(mode, data):
    '''
    Opens physics_data.txt for viewing or updating data
    
    If mode is "r" then read physics_data.txt
    If mode is "a" then append to physics_data.txt
    '''
    
    r = open("physics_data.txt", mode)
    
    # if entered mode is "r," read mode, then we will read the physics data
    if mode == "r":
        print("DATA")
        lines = r.readlines()
        for x, line in enumerate(lines):
            print(str(x + 1) + ". " + line[:-1])
        program_output(["DATA"] + [str(x + 1) + ". " + line[:-1] for x, line in enumerate(lines)])
    
    # if entered mode is not "r," then it is "a," append mode, and we will append to physics data
    else:
        r.write(str(data[0]) + " = " + str(data[1]) + "\n")
        
    r.close()


def add_data(data = None):
    '''
    Adds data to physics_data.txt
    
    data is the variable value that will be added
    if data == None, the user will be asked in this function for the value
    else, this function has been called from another that has already calculated a value
    '''
    
    # prompt user for name of variable
    name = input("Name of Variable: ")
    
    # if no data was given, then we will prompt user for data (value of variable) and update program output file (log)
    if data == None:
        data = input("Value: ")
        program_output(["Name of Variable: " + name, "Value: " + str(data)])
    # if data was given, update program output file (log)
    else:
        program_output(["Name of Variable: " + name])
    
    # append new variable name and value to physics data
    open_data("a", [name, data])
    

# -------------------------------------------
# CALCULATIONS
# -------------------------------------------

def is_number(values):
    '''
    Checks if the elements in the list "values" are numbers
    
    Return True if all values are numbers
    Return False otherwise
    '''
    
    # try to turn every element in the list of values into a float,
    # if an error occurs, it is not a number
    try:
        for value in values:
            float(value)
        return True
    except:
        space()
        print("One of the values is not valid.")
        program_output("One of the values is not valid.")
        return False


def momentum():
    '''
    Calculates p, momentum
    Return calculated p if user input valid values
    '''
    
    print("CALCULATING MOMENTUM")
    # prompts user for variable input, assumes that the user will input a positive value for mass
    mass = input("MASS (kg), numbers only: ")
    speed = input("SPEED (m/s), numbers only: ")
    
    # updates program output log
    program_output(["CALCULATING MOMENTUM",
                    "MASS (kg), numbers only: " + str(mass),
                    "SPEED (m/s), numbers only: " + str(speed)])
    
    # calls function is_number to check that the variable input given are numbers (int or float)
    # if True, return the calculated data
    # if False, return None
    if is_number([mass, speed]):
        return "Momentum (p) = ", float(mass) * float(speed), " kg * m/s"
    else:
        return None


def change_in_momentum():
    '''
    Calculates delta_p, change in momentum
    Return calculated delta_p if user input valid values
    '''
    
    print("CALCULATING CHANGE IN MOMENTUM")
    # prompts user for variable input, assumes that the user will input a positive value for time
    fnet = input("FNET (N), numbers only: ")
    time = input("TIME (s), numbers only: ")
    
    # updates program output log
    program_output(["CALCULATING CHANGE IN MOMENTUM",
                    "FNET (N), numbers only: " + str(fnet),
                    "TIME (s), numbers only: " + str(time)])
    
    # calls function is_number to check that the variable input given are numbers (int or float)
    # if True, return the calculated data
    # if False, return None
    if is_number([fnet, time]):
        return "Change in Momentum (delta_p) = ", float(fnet) * float(time), " kg * m/s"
    else:
        return None
    

def final_momentum():
    '''
    Calculates pf, final momentum
    Return calculated pf if user input valid values
    '''
    
    print("CALCULATING FINAL MOMENTUM")
    # prompts user for variable input, assumes that the user will input a positive value for time
    pi = input("INITIAL MOMENTUM (kg * m/s), numbers only: ")
    fnet = input("FNET (N), numbers only: ")
    time = input("TIME (s), numbers only: ")
    
    # updates program output log
    program_output(["CALCULATING FINAL MOMENTUM",
                    "INITIAL MOMENTUM (kg * m/s), numbers only: " + str(pi),
                    "FNET (N), numbers only: " + str(fnet),
                    "TIME (s), numbers only: " + str(time)])
    
    # calls function is_number to check that the variable input given are numbers (int or float)
    # if True, return the calculated data
    # if False, return None
    if is_number([pi, fnet, time]):
        return "Final Momentum (pf) = ", float(pi) + (float(fnet) * float(time)), " kg * m/s"
    else:
        return None
    

def final_velocity():
    '''
    Calculates vf, final speed
    Return calculated vf if user input valid values
    '''
    
    print("CALCULATING FINAL SPEED")
    # prompts user for variable input, assumes that the user will input a positive value for time and mass
    vi = input("INITIAL SPEED (m/s), numbers only: ")
    fnet = input("FNET (N), numbers only: ")
    time = input("TIME (s), numbers only: ")
    mass = input("MASS (kg), numbers only: ")
    
    # updates program output log
    program_output(["CALCULATING FINAL SPEED",
                    "INITIAL SPEED (m/s), numbers only: " + str(vi),
                    "FNET (N), numbers only: " + str(fnet),
                    "TIME (s), numbers only: " + str(time),
                    "MASS (kg), numbers only: " + str(mass)])
    
    # calls function is_number to check that the variable input given are numbers (int or float)
    # if True, return the calculated data
    # if False, return None
    if is_number([vi, fnet, time, mass]):
        return "Final Velocity (vf) = ", float(vi) + (float(fnet) * float(time) / float(mass)), " m/s"
    else:
        return None


def calculate():
    '''
    Menu for calculations
    Display equation options
    '''
    
    equations_menu = ["Enter the number of the corresponding option.",
                      "For example, enter '1' for momentum (p).",
                      "----------------------------------------------------",
                      "1. p = mv",
                      "2. delta_p = fnet*delta_t",
                      "3. pf = pi + fnet*delta_t",
                      "4. vf = vi + fnet*delta_t/m",
                      "Type anything else to exit.",
                      "----------------------------------------------------",]
    for line in equations_menu: print(line)
    # input for the menu option the user wishes to select
    choice = input("CHOICE: ")
    
    # calculated will be a tuple (initially set to None) containing information from user's desired equation:
    # consisting of the name of what was calculated, the calculated value, and the unit
    # EX: // Selecting for momentum will return: ("Momentum (p) = ", [calculated p], " kg * m/s")
    calculated = None
    
    # updates program output file with the user's selection
    program_output(equations_menu + ["CHOICE: " + choice])
    space()
    
    # call function corresponding to user's desired equation
    if choice == "1":
        calculated = momentum()
    elif choice == "2":
        calculated = change_in_momentum()
    elif choice == "3":
        calculated = final_momentum()
    elif choice == "4":
        calculated = final_velocity()
    
    if calculated != None:
        space()
        
        # prints the calculated value of the equation and other information associated
        # at index 0 is the name of what was calculated, EX: // "Momentum (P)"
        # at index 1 is the calculated value
        # at index 2 is the corresponding unit of measurement to the calculated value, EX : // " kg * m/s"
        print(calculated[0], str(calculated[1]), calculated[2])
        
        # ask user if they wish to save the calculated value in physics_data.txt
        print("Type 'y' to save this to your data. Type anything else to not save.")
        choice = input("CHOICE: ")
        # update program output file with the calculated data
        program_output([calculated[0] + str(calculated[1]) + calculated[2],
                        "Type 'y' to save this to your data. Type anything else to not save.",
                        "CHOICE: " + choice])
        space()
        
        # if the user wishes to save the calculated value (choice is "y") then call function to add it to physics_data
        if choice == "y":
            add_data(calculated[1])
    

# -------------------------------------------
# MAIN
# -------------------------------------------

def main():
    '''
    Main menu of program
    Display menu options
    '''
    
    main_menu_text = ["MOMENTUM PRINCIPLE CALCULATIONS",
                      "----------------------------------------------------",
                      "What would you like to do?",
                      "Enter the number of the corresponding option.",
                      "For example, enter '1' to Calculate.",
                      "----------------------------------------------------",
                      "1. Calculate",
                      "2. Add Data",
                      "3. Read Data",
                      "4. Exit"]
    
    run = True
    while run:
        for line in main_menu_text: print(line)
        choice = input("CHOICE: ")
        
        program_output(main_menu_text + ["CHOICE: " + choice])
        space()
        
        if validate(choice, ["1", "2", "3", "4"]):
            
            if choice == "1":
                calculate()
            elif choice == "2":
                add_data()
            elif choice == "3":
                open_data("r", None)
            else:
                run = False
        
        space()
    

# -------------------------------------------
# END OF FUNCTIONS
# -------------------------------------------

# creates a program output file if it doesn't already exist
# if it exists, overwrite it to be empty
t = open("cps109_a1_output.txt", "w")
t.close()

# creates a physics data text file if it doesn't already exist
# if it exists, overwrite it to be empty
new = open("physics_data.txt", "w")
new.close()

# runs program
main()

# outputs when program is done running
print("Program is done running.")
program_output("Program is done running.")