import random 



def dice(): 
    total = 120 
    game = "Y" 
 
    while (game == "Y"or game =="y"):
        print (" you have = ", total, "Gold")
        bbet = input("how much do you bet ? : ") 
        bet = int(bbet)
        while bet > total:
            print("You don't have the money, Please bet again")
            bbet = input("how much do you bet ?") 
            bet = int(bbet)
        print ("""  \_1_/  \_2_/  \_3_/  """)
        guess= input("Which pot is the stone in ? : ")
        guess=int(guess)
        while guess >3:
            print("It is out of 3 !!")
            bbet = input("how much do you bet ? : ") 
            bet = int(bbet)
        die1 = random.randint(1,3) 
        print ("It is under pot ", die1) 
        if die1 !=guess: 
            print ("You lose") 
            total-=bet 
        else: 
           print ( "You win") 
           total+=bet*3 

        if total<=0:
            print("Go home you have no more gold left ")
            break
        game = input("Play again? (Y/N)")
        game= game.upper()

        if game== "N":

            print (" final amount = ", total, "Gold")
            print("Good bye")


dice()