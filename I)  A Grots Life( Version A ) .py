

import random

lootlist=["Fist Full of Straws","Fish Bone","Old Stick","Dirty Potato Sack","Crumbling Stones","Rusty Umbrella","Rope"]
enemylist=("Rat","Hobbit","Tiny Dragon","Drunk Human","Killer Bee")
inventory=[]
food=("Mushrooms","Meaty Bones","Rotten Apples","Spoiled Meat")
larder=[]
goal=[]

# Class defines an object

#self represents the instance of the class.
#When objects are instantiated, the object itself is passed into the self parameter.
#Because of this, the object’s data is bound to the object

# __init__ ( known as a constructor or initialization method)
# This automatically invoked when new object is created.
# All class will have a method __init__ which provide instructions on what arguments is needed
# eg: gob = Goblin(gob_name,0,100,0,20) which is the goblin's name,hunger,health,provision,gold
# can invoke functions/methods but in this case just intialize attribute values 


class Goblin(object):

    
    def __init__(self, name, hunger,health,provision,gold ):       
        self.name = name                                         
        self.hunger = hunger
        self.health= health
        self.provision= provision
        self.gold=gold

    def __pass_time(self):
        self.hunger += 1

    
    @property
    def hung(self):

        hung=self.hunger
        
        if  hung<5:
             m=("not hungry")
        elif 5 <=hung <=10:
             m=(" a bit hungry")
        elif 11 <=hung<=15:
             m=("hungry")
        else:
            m= (" staving !!!")

        return m
     
    @property
    def wounded(self):
        
        cod=self.health
        
        if  cod==100:
            d=("fighting fit !!")
        elif 70 <=cod <=99:
            d=("in good health")
        elif 40<=cod<=69:
            d=(" bleeding bad")
        else:
            d=("very wounded")

        return d

    
    def status(self):
    
        print("You have",self.provision,"provisions")
        print("You have",inventory,"in your bag" )
        print("You have",self.gold, "gold")
        print("You are ",self.hung)
        print("You are ",self.wounded)
        self.__pass_time()

 
        
    def eat(self, eat = 5):
     
        if self.hunger<=0:
            print("You are not hungry")

        elif self.provision>0:            
            mep=random.choice(larder)
            print("You eat some",mep)
            larder.remove(mep)
            print("It was a tasty meal")
            self.hunger -= eat
            self.provision-=2
                   
      
        else:
            print("You do not have any food")
            

        self.__pass_time()
      
        
    def hunt(self):
       
        loot=random.choice(lootlist)
        enemy=random.choice(enemylist)
        if ("Fish Bone Spear") in goal:
            print("Armed with your Fish Bone Spear...")
            damage=random.randint(1,10)
            self.health-=damage
            
        else:
            damage=random.randint(11,30)
            self.health-=damage
            
        print ("You came across a",enemy)
        print("After an epic fight you took ",damage,"damage")         

        if loot in inventory:
            print("You see nothing of interest")
            
        else:
            inventory.append(loot)
            print("But you find",loot)

        coin=random.randint(1,5)
        self.gold+=coin
        print("You have gain",coin,"gold")
        
        self.__pass_time()
        


    def farm(self,stash=2):
        grub=random.choice(food)
        print("You have found some",grub)
        larder.append(grub)
        print("You have gained",stash,"provisions")
        self.provision+= stash
    
        self.__pass_time()
      
        
    def rest(self):
     
        if self.health>=100:
            print("You do not need rest")

        else:
      

            if("Straw Bed") in goal:
                print("You rest better in your Straw Bed")
                sleep=random.randint(10,30)
                

            else:
                print("Sleeping on the floor is rough ")
                sleep=random.randint(5,20)
             

            bob=self.health
            self.health+=sleep

            if self.health>=100:
                self.health=100

            recover= self.health-bob   
            print("You have recovered",recover,"health")

        self.__pass_time()
        

    def craft(self):
        print( """
                0-exit
                1-Fish Bone Spear
                2-Straw Bed
                3-Small Hut 
                
              
                 """)



        choice=input("Choice:")

        if choice == "0":
            print("come back when you have more resource")

        elif choice=="1":
            if ("Fish Bone Spear") in goal:
                print("You only need one")

            elif "Fish Bone" and "Old Stick" in inventory:
                inventory.remove("Fish Bone")
                inventory.remove("Old Stick")
                goal.append("Fish Bone Spear")
                print("You have crafted the Fish Bone Spear")
                
            else:
                print("You do not have the crafting material")

        elif choice=="2":

            if ("Straw Bed") in goal:
                print("You only need one")

            elif "Fist Full of Straws" and "Dirty Potato Sack" in inventory:
                inventory.remove("Fist Full of Straws")
                inventory.remove("Dirty Potato Sack")
                goal.append("Straw Bed")    
                print("You have crafted Straw Bed")

            else:
                print("You do not have the crafting material")

        elif choice=="3":

            if ("Small Hut") in goal:
                print("You only need one")

            elif "Crumbling Stones" and "Rusty Umbrella" and "Rope" in inventory:
                inventory.remove("Crumbling Stones")
                inventory.remove("Rusty Umbrella")
                inventory.remove("Rope")
                goal.append("Small Hut")    
                print("You have crafted Small Hut")

            else:
                print("You do not have the crafting material")



        else:
            print("invalid")
           
        
def main():
    
    gob_name = input("What do you want to name your Goblin?: ")
    gob = Goblin(gob_name,0,100,0,20)

    endgame = False
    choice = None  
    while choice != "0":
        print (  "  So... "  ,gob_name, " What is your action ?" )
        print \
        ("""
    
        0 - Quit
        1 - status
        2 - Eat
        3 - Scavenge 
        4 - Explore
        5 - Rest
        6 - Craft 
        """)
    
        choice = input("Choice: ")
        print()

    
        if choice == "0":
            print("Good-bye.")


        elif choice == "1":
            gob.status()
        

        elif choice == "2":
            gob.eat()

        elif choice == "3":
            gob.farm()

        elif choice == "4":
            gob.hunt()

        elif choice == "5":
            gob.rest()

        elif choice == "6":
            gob.craft()
            
        else:

            print("\nSorry, but", choice, "isn't a valid choice.")

        if gob.hunger >20:
            print("died from hunger")
            input("press any button to continue")
            break

        if gob.health <=0:
            print("died from wounds")
            input("press any button to continue")
            break

        
        if endgame == False:
            if ("Fish Bone Spear") in goal and ("Straw Bed")in goal and("Small Hut") in goal:
                print("You have built your home and prove you are a survivor, you win !!")
                con=input("Do you want to continue playing 1-yes, 2-no" )
                if con == "1":
                    endgame = True

                elif con == "2":
                    print("Good bye")
                    break

                else:
                    pass

            else:
                pass
 
        else:
            pass 
                  

 
main()
("\n\nPress the enter key to exit.") 
