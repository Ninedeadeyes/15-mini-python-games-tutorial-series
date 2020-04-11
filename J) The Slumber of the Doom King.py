import random
import time


# Stats 
health=100
gold=0
alive=True
encounter1=False   # This is used so that unique encounter only happen once. 


# Game Title :  The Slumber of the Doom King

# function that provides input from player 

def input_direction():
    direction1 = input("Which direction do you want to go? ")
    direction=direction1.lower()
    while direction not in ["north", "south", "east", "west", "exit"]:
        direction1 = input("Invalid answer,which direction do you want to go? ")
        direction=direction1.lower()

    return direction   # When you execute input_direction it will return 'the direction' eg: north,south,east,west 
                       # Return statement is used in a function to return something to the caller program.

def nothing():
    pass

def jester():


    
    global encounter1   # If you do not use global the encounter within the function is consider a local variable
                       # and you will have a "local variable referenced before assignment error" 

    
    while encounter1==False: 
    
        print ("You see a sad jester in the corner of the room")
        print ("He ask you a question")
        question1=input("Can you spare me some life for some gold ? Y or N")
        question=question1.lower()
        
        if question=="y" or question=="yes":
            global life
            global gold 
            life=-10
            gold=+300
            print("The Jester smile and say 'thank you'.")
            print("You lose 10 life ")
            print("You gain 300 gold")
            encounter1=True

            
        else:
            print("The Jester scream at you 'go away!' ")
            encounter1=True
    else:
        pass





# Introduction 


print ("                      The Slumber of the Doom King  ")
print("                                                                                   ")
print("Goal: Steal as much gold as possible and escape the castle of the Doom King before he consume your soul !!")
print("Direction: North/East/South/West/Quit")

time.sleep(1.5)

#function




# Set up the Locations


compass = dict({ "north" : {1:-1,2:-1,3:-1,4:-1,5:1,6:2,7:3,8:4,9:5,10:6,11:7},
                 "east":  {1:2,2:3,3:4,4:-1,5:6,6:7,7:8,8:-1,9:10,10:11,11:12},
                 "south": {1:5,2:6,3:7,4:8,5:9,6:10,7:11,8:12,9:-1,10:-1,11:-1},
                 "west": {1:-1,2:1,3:2,4:3,5:-1,6:5,7:6,8:7,9:-1,10:9,11:10}
                })

descr = dict({
              1: "Location: Master bedroom. You feel something is watching you",
              2: "Location: Nursery. There is a sense of forelorn here",
              3: "Location: Treasury. It has been ransacked a long time ago",
              4: "Location: Library. It is filled with books of black magic   ",
              5: "Location: Dining room. Someone has been here recently",
              6: "Location: Torture chamber. You feel sick with dread...",
              7: "Location: Garden. All flowers has withered and died ",
              8: "Location: Burial Chamber. Something should be forgotten",
              9: "Location: Armoury. Filled with a assortment of demonic weapons",
             10: "Location: Kitchen. Old pots and pans clutters the room ",
             11: "Location: Servant Quarter. A skeleton lies on the floor, a sad sight",
             12: ""})


# Unique events ( You can add different types of quests/storylines/characters for each location

events = dict({
              1: nothing,
              2: jester,
              3: nothing,
              4: nothing,
              5: nothing,
              6: nothing,
              7: nothing,
              8: nothing,
              9: nothing,
             10: nothing,
             11: nothing,
             12: nothing,}) 



currentRoom = 1



# Game loop
while alive==True:

    # Describe the current room
    print (descr[currentRoom])
    events[currentRoom]()
    
    
    loot=random.randrange(1,20)
    loot1=str(loot)
    print ("you find",loot1,"gold")
    gold+=loot
    print ("Total gold:",gold)
    print("Life:",health)


    # See if you awake the Doom King or not 
    sleep=random.randint(1,9)

    if sleep ==5 and currentRoom !=12:
        damage=random.randrange(30,60)
        health-=damage        
        print("The Doom King is awake, he attacks you !!")
        print("Life:", health)
        if health <=0:
            print("The Doom King consume your soul and break your body.( THE END )")
            input("Press enter to escape")
            break
        else:
            print("Thankfully you escape and the King falls back into slumber")
            
            

    elif sleep==1 or sleep==2:
        print("You hear the Doom King groan but then silence")

    elif sleep==3 or sleep==4:
        print("The Doom King is left undisturbed")

    elif sleep==6 or sleep==7:
        print("The Doom King remains asleep")

    else:
        print( "The Doom King slumber..") 



    # calling the function of user input, works because the 'return' function was used 
    newDir = input_direction()
    
     

    # If you wish to exit
    if newDir == "quit":
        print ("Good bye")
        break
    else:

        # Otherwise look up whether there is a path that way
        if compass[newDir][currentRoom] != -1:
            currentRoom = compass[newDir][currentRoom] # eg: compass[east][1] will return value 2 
            print(newDir)  # This is just to demonstrate how 'return' works, can delete if you want 
        else:
            print ("There is no path in that direction")
        # If you find the exit 
        if  currentRoom ==12:
            print("Location: Exit Gate. You have found the exit, well done !!")
            print("Total gold:",gold," can you do better next time?")
            input("Press enter to escape")
            break






        
        


