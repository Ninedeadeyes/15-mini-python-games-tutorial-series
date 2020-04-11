from info import*                # *import all elements from the module 
from mood import hung,wounded    # Can import specific hence leaving out the function 'left_behind
import random                    # if just import module no import instruction
                                 # then need to write module and method name 
                                 # for example : random.choice or random.randint
                      

class Goblin(object):
   
    
    
    def __init__(self, name, hunger,health,provision,gold ):
        self.name = name
        self.hunger = hunger
        self.health= health
        self.provision= provision
        self.gold=gold
        self.inventory=[]
        self.goal=[]
        self.larder=[]
        

    def __pass_time(self):
        self.hunger += 1

    

    
    def status(self):
        print("Inventory")
        for x in range(len(self.inventory)):
            print (self.inventory[x],)
        print("You have",self.provision,"provisions")
        #print("You have",self.inventory,"in your bag" )
        print("You have",self.gold, "gold")
        print("You are",hung(self.hunger))
        print("You are",wounded(self.health))
        self.__pass_time()

 
        
    def eat(self, eat = 5):
     
        if self.hunger<=0:
            print("You are not hungry")

        elif self.provision>0:            
            mep=random.choice(self.larder)
            print("You eat some",mep)
            self.larder.remove(mep)
            print("It was a tasty meal")
            self.hunger -= eat
            self.provision-=2
                   
      
        else:
            print("You do not have any food")
            

        self.__pass_time()
      
        
    def explore(self):
        loot=random.choice(lootlist)
        enemy=random.choice(enemylist)
        if ("Fish Bone Spear") in self.goal:
            print("Armed with your Fish Bone Spear...")
            damage=random.randint(1,10)
            self.health-=damage
            
        else:
            damage=random.randint(11,30)
            self.health-=damage
            
        print("You come across a",enemy)
        print("After an epic fight, you defeat the",enemy)
        print("you took",damage,"damage")         

        if loot in self.inventory:
            print("You see nothing of interest")
            
        else:
            self.inventory.append(loot)
            print("You find a",loot)

        coin=random.randint(1,5)
        self.gold+=coin
        print("You gain",coin,"gold")
        
        self.__pass_time()
        


    def farm(self,stash=2):
        grub=random.choice(foodlist)
        print("You find some",grub)
        self.larder.append(grub)
        print("You gain",stash,"provisions")
        self.provision+= stash
    
        self.__pass_time()
      
        
    def rest(self):
     
        if self.health>=100:
            print("You do not need rest")

        else:
      

            if("Straw Bed") in self.goal:
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
            print("You have recover",recover,"health")

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
            if ("Fish Bone Spear") in self.goal:
                print("You only need one")

            elif "Fish Bone" and "Wood Stick" in self.inventory:
                self.inventory.remove("Fish Bone")
                self.inventory.remove("Wood Stick")
                self.goal.append("Fish Bone Spear")
                print("You have crafted the Fish Bone Spear")
               
            else:
                print("You do not have the crafting material")
               
        elif choice=="2":

            if ("Straw Bed") in self.goal:
                print("You only need one")
                
            elif ("Fist Full of Straws") and ("Dirty Potato Sack") in self.inventory:
                self.inventory.remove("Fist Full of Straws")
                self.inventory.remove("Dirty Potato Sack")
                self.goal.append("Straw Bed")    
                print("You have crafted Straw Bed")

            else:
                print("You do not have the crafting material")

        elif choice=="3":

            if ("Small Hut") in self.goal:
                print("You only need one")

            elif ("Giant Boot") and ("Rusty Umbrella") in self.inventory:
                self.inventory.remove("Giant Boot")
                self.inventory.remove("Rusty Umbrella")
                self.goal.append("Small Hut")    
                print("You have crafted Small Hut")

            else:
                print("You do not have the crafting material")



        else:
            print("invalid")
        

