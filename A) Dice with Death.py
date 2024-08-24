import random, sys     # This 'import' the random and sys module which will be used in the programme 
                       # This will provide acces additional functions/modules within the module.
                       #  From example : random.randint  and sys.exit()
def intro():

    print("You are playing dice with death")
    print("Win and live another day, lose and your soul is doomed")

    input("press enter to continue")   # Allows user to 'input' info but because it is not tied to a variable 
                                       # the info is lost. In this instance it is used as to 'pause' 
def game():

    print("death rolls first")
    death_roll=random.randint(1,12)   # 'randint' is an example of a method .A method is a function that is tied
    print( "death rolls",death_roll)  #  to an object ( which is random)
    input("press enter to continue")  
    your_roll=random.randint(1,12)
    print("you roll",your_roll)
    input("press enter to continue")

    while death_roll == your_roll:
        print("you will need to play again")
        game()

    if death_roll>your_roll:
        print("You lose the game and your life")
        
    if your_roll>death_roll:
        print("You win and live another day")

    play_again = input("Play again? (yes/no)")
    play_again= play_again.lower()

    if play_again =="no":                               # Simple example of if statement.  If you type in 'no' it will quit the game
        input("Good bye, press enter to quit ")
        sys.exit()         

    intro()                              
    game()

intro()                                 # A function will need to be 'called'/invoked before it does anything, eg: intro(),game()  
game()                                  

#Variables 

# A variable is a container for storing data values. It is like a box to store something 
# example :  death_roll is a variable. A dice roll between 1 to 12 will be stored within the variable 'death_roll'
# In the next game 'Hacker' I will be providing more examples of variables. 

# Functions 

# A function is a block of organized,
# reusable code that is used to perform a single, related action
# They are like little machines that needs to be switched on (invoked/called) before they do anything 

# def intro() is a user defined function (created by the user)

# print and input are examples of inbuilt functions.


# Conditional Statements

# If statement 

# The if statement is the most simple decision-making statement. It is used to decide whether a certain statement
# or block of statements will be executed or not.

#https://github.com/Ninedeadeyes/15-mini-python-games-
