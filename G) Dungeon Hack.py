import random

def game():
    print("Choose your party and enter the dungeon")
    print("to slay the beast and steal his treasure !! ")
    print("")

    print( "Fighter, ","Wizard, ","Thief, ","Paladin, ","Rogue ")


    group=[]

    more_items= True

    loop=0

    power=0

    scout=0

    magic=0

    while more_items:


        
        user_input=input("who are you going to take with you ? : ")
        user_input=user_input.upper()


        if user_input=="FIGHTER":
           print("you have chosen the Fighter")
           group.append(user_input)
           power+=5
        

        elif user_input=="THIEF":
           print("you have chosen the Thief")
           group.append(user_input)
           scout+=5

        elif user_input=="WIZARD":
           print("you have chosen the Wizard")
           group.append(user_input)
           magic+=5
        
        elif user_input=="ROGUE":
           print("you have chosen the rogue")
           group.append(user_input)
           scout+=random.randint(2,5)
           power+=random.randint(2,5)     

        elif user_input=="PALADIN":
           print("you have chosen the Paladin")
           group.append(user_input)
           power+= random.randint(2,5)
           magic+= random.randint(2,5)

        else:
            print("not a valid choice, but don't worry i'll pick someone for you")
            list=("VILLAGE IDIOT","SNOTLING JESTER","PROFESSIONAL COWARD","SAD CLOWN")
            wildcard=random.choice(list)
            group.append(wildcard)
            power+= random.randint(1,3)
            magic+=random.randint(1,3)
            scout+=random.randint(1,2)
   
     
            
        loop+=1

        if loop==4:
           more_items= False

       
    print("Your party is full, it is time to begin your adventure")
    print("You party consist of:")
    for x in range(len(group)):     # This only really numbers your characters in your group  
        print (x+1,group[x])        # For x in range = For every 'item' in the group  
                                    # x+1 because range starts at 0, group[x]=acquire the value
                                    # of the 'item' which will be PALADIN,ROGUE etc etc 

    dungeon=input(" Pick dungeon: Hard or Easy ?")
    dungeon=dungeon.lower()

    input("You go into the dungeon and.... ")

    if dungeon== "hard":

        if power>=12 and scout>=5 and magic>=7:
            print ("You slay the beast and find the treasure !!, you win all the loot  ")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)

        elif  power>12 and scout>=5 and magic<7:
            print("You slay the beast but did not find any treasure, you lose")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)
        else:
            print("you are defeated by the beast, your party was too weak, you lose ")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)

        print("Game over")
        play=input("play again Y/N ? : ")
        play.lower()
        if play == "y":
            game()
        else:
            print("good bye")
            quit()



    else:    
   

        if power>=10 and scout>=5 and magic>=5:
            print ("You slay the beast and find the treasure !!, you win, try the hard dungeon ")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)

        elif  power>10 and magic>=5 and scout<5:
            print("You slay the beast but did not find any treasure, you lose")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)
        else:
            print("you are defeated by the beast, your party was too weak, you lose ")
            print ("Your party stats are : power=",power, "scout=",scout,"magic=",magic)

        print("Game over")
        play=input("play again Y/N ? : ")
        play.lower()
        if play == "y":
            game()
        else:
            print("good bye")
            quit()


game()
    
