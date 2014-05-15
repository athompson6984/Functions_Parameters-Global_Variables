#Dice roll
#This program rolls a dice before displaying it to the user, in the appearance of a dice face.

import random,time
#This imports random to make the number rolled a random number (between 1 and 6 inclusive)
#This imports time to add a pause between generating the random number and printing it to the user.

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"
#All of these variables, when printed, display the face of the dice that the random number is.

def rollnumber():
    #This function generates a random number between 1 and 6 inclusive, turning it into a variable.
    print("rolling.....")
    global roll #This makes it global so that it can be used in other functions.
    roll = random.randint(1,6)

def show_dice(roll): #This uses the random number to print off the right face.
    if roll == 1:
        print(s1) #These print lines display the correct face to the user.
    elif roll == 2: #The original code used else, however this is not correct as we need more than 2 options.
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)

#This part of the program runs the functions in the correct order
#It is therefore the main part of the program.
rollnumber()
time.sleep(1)
show_dice(roll)

###Some of the errors that I found were:
    # when importing modules, it put a ; between the requested imports rather than a ,
    # The rollnumber function was orifinally called roll, the same as a variable that was being used inside the function.
    # import was misspelt
    # They used the wrong use of the random generator. I changed it to random.randint(1,6), which made it generate a random integer between 1 and 6 inclusive.
    # the show_dice() function did not request a parameter
