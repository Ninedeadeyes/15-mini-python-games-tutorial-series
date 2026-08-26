import random 

def dice(): 
    total = 120 
    game = "Y" 
 
    while (game == "Y"or game =="y"):
        print (" you have = ", total, "Gold")
        bbet = input("how much do you bet ? : ") 
        bet = int(bbet)  # Turns the input into a 'number value' from a string value because a string can't interact with an integer (whole number)
        while bet > total:
            print("You don't have the money, Please bet again")
            bbet = input("how much do you bet ?") 
            bet = int(bbet)

        print (r"""  \_1_/  \_2_/  \_3_/  """)    #  Prefix the string with an r to treat it as a raw string, which tells Python not to interpret escape sequences within the string.
        guess= input("Which pot is the stone in ? : ")
        guess=int(guess)
        while guess >3:
            print("It is out of 3 !!")
            guess= input("Which pot is the stone in ? : ")
            guess=int(guess)
        die1 = random.randint(1,3) 
        print ("It is under pot ", die1) 
        if die1 !=guess: 
            print ("You lose") 
            total-=bet 
        else: 
           print ( "You win") 
           total+=bet*2 

        if total<=0:
            input("Go home you have no more gold left, press enter to escape ")
            break        # Automatically break the while loop hence ending the game 
        game = input("Play again? (Y/N)")    # At the end of each game will ask if player want to play again 
        game= game.upper()

        if game== "N":                              # If player answer N, it will break the loop because game has to be Y   
                                                    # Will finish the loop hence provide final amount of gold before breaking.  
            print (" final amount = ", total, "Gold")
            input("Good bye, press enter to escape")

dice()

#https://github.com/Ninedeadeyes/15-mini-python-games-
