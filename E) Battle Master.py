import time, random
counter=0
player1=0
player2=0


def player1_win():
    print("Orcs win the battle")
    global player1        # Generally speakin Global function is the worst 
    player1+=1            # approach to interact with variable outside the 
                          # function but its good to know how to do it 
def player2_win():        # Better methods is using data structure like list or CLASS 
    print("Humans win the battle")
    global player2
    player2+=1


while True:

    print("""The war between Orcs and Humans rage on forever
    "You are the new commander, you have 100 men which you have to
    allocate to the apprioate position to win the war """)

    #The try and except block in Python is used to catch and handle exceptions.      

    while True:  
        knight=input("how many Knights ?")
        try:
            int(knight)
            break

        except:        
            print("This is not a number")


    while True: 
        farmer=input("how many Farmers ?")
        try:
            int(farmer)
            break

        except:
            print("This is not a number")
                

    while True:
        defender=input("how many Defenders ?")
        try:
            int(defender)
            break

        except:
            print("This is not a number")


    
    tog=int(defender)+int(farmer)+int(knight)
    
    if tog>100:
        print("You have allocated over 100")

    else:
        print("You have",str(defender),"Defenders.You have",str(farmer),"Farmers and"
              ,str(knight),"Knights")
        break 

            
    
     


while True:
    

    while True:
        counter+=1
        print("The battle rages on and on ..")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        print("...")

        if counter==3:
            break

    print("A victor has been decided")

    x=random.randint(1,3)

    time.sleep(x)

    defender1=int(defender)+random.randint(1,15)
    farmer1=int(farmer)+random.randint(1,10)
    knight1=int(knight)+random.randint(1,15)

    

    if defender1>=38 and farmer1>=15 and knight1>=55:
        player2_win()

    else:
        player1_win()

    print("Orc victory:"+str(player1)+" Human victory:"+str(player2))
    counter=0

    if player1==5:
        print("""The Orcs has won the war. You have been defeated !!""")
        
        break

    
        

    if player2==5:
        print("The Humans has won the war, congratulations !!")
        
        break


input("Press enter to exit")
        
        



  

        



    
