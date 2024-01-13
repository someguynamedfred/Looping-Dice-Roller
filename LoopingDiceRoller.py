import random

print ("Welcome to my random number generator.\n\n")

#this is for general dice rolls
while True:

    n1 = input ("What would you like to do? ")
    if n1 == "roll" or n1 == "r":
        diceroll = input ("\nHow many sides on the dice? ")
        if diceroll == "exit":
            exit ()
        n2 = random.randint (1, int(diceroll))
        n3 = input ("\nWhat is the modifier? ")
        if n3 == "":
            n3 = 0
        n4 = (int(n2) + int(n3))
        print ("\nYou rolled a " + str(n2) + " + " + str(n3) + " = " + str(n4)) 
        input ("\nYour total is " + str(n4) + "\n\n")
    if n1 == "exit":
        exit ()
    else:
        print ("Let's roll some dice \n")
        n1 = "roll"
