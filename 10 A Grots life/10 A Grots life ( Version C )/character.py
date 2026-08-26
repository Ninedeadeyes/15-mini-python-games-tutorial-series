
import random 

class Goblin:
    def __init__(self, name, hunger, health, provision, gold, data):       
        self.name = name                                         
        self.hunger = hunger
        self.health = health
        self.provision = provision
        self.gold = gold
        self.data = data
        self.inventory = []
        self.larder = []
        self.goal = []

    def __pass_time(self):
        self.hunger += 1
  
    @property
    def hung(self):
        if self.hunger < 5:
            return "not hungry"
        elif 5 <= self.hunger <= 10:
            return "a bit hungry"
        elif 11 <= self.hunger <= 15:
            return "hungry"
        else:
            return "starving !!!"
     
    @property
    def wounded(self):
        if self.health == 100:
            return "fighting fit !!"
        elif 70 <= self.health <= 99:
            return "in good health"
        elif 40 <= self.health <= 69:
            return "bleeding bad"
        else:
            return "very wounded"

    def status(self):    
        print(f"You have {self.provision} provisions")
        print(f"You have {self.inventory} in your bag" )
        print(f"You have {self.gold} gold")
        print(f"You are {self.hung}")
        print(f"You are {self.wounded}")
        self.__pass_time()

    def eat(self, eat=5):     
        if self.hunger <= 0:
            print("You are not hungry")
        elif self.provision > 0 and self.larder:
            meal = random.choice(self.larder)
            print("You eat some", meal)
            self.larder.remove(meal)
            print("It was a tasty meal")
            self.hunger -= eat
            self.provision -= 2
        else:
            print("You do not have any food")
        self.__pass_time()
      
    def hunt(self):
        loot = random.choice(self.data.lootlist)
        enemy = random.choice(self.data.enemylist)
        
        if "Fish Bone Spear" in self.goal:
            print("Armed with your Fish Bone Spear...")
            damage = random.randint(1,10)
        else:
            damage = random.randint(11,30)
        self.health -= damage
            
        print (f"You came across a {enemy}")
        print(f"After an epic fight you took {damage} damage")       

        if loot in self.inventory:
            print("You see nothing of interest")
        else:
            self.inventory.append(loot)
            print(f"But you find {loot}")

        coin = random.randint(1,5)
        self.gold += coin
        print(f"You have gain {coin} gold")
        self.__pass_time()
        
    def farm(self, stash=2):
        grub = random.choice(self.data.food)
        print(f"You have found some {grub}")
        self.larder.append(grub)
        print(f"You have gained {stash} provisions")
        self.provision += stash
        self.__pass_time()
      
    def rest(self):
        if self.health >= 100:
            print("You do not need rest")
        else:
            if "Straw Bed" in self.goal:
                print("You rest better in your Straw Bed")
                sleep = random.randint(10,30)
            else:
                print("Sleeping on the floor is rough")
                sleep = random.randint(5,20)

            original_hp=self.health
            self.health+=sleep

            if self.health>=100:
                self.health=100

            recover= self.health-original_hp  
            print(f"You have recovered {recover} health")
        self.__pass_time()
        
    def craft(self):
        print("""
                0-exit
                1-Fish Bone Spear
                2-Straw Bed
                3-Small Hut 
        """)
        choice = input("Choice:")

        if choice == "0":
            print("Come back when you have more resources")
        elif choice == "1":
            if "Fish Bone Spear" in self.goal:
                print("You only need one")
            elif "Fish Bone" in self.inventory and "Old Stick" in self.inventory:
                self.inventory.remove("Fish Bone")
                self.inventory.remove("Old Stick")
                self.goal.append("Fish Bone Spear")
                print("You have crafted the Fish Bone Spear")
            else:
                print("You do not have the crafting material")
        elif choice == "2":
            if "Straw Bed" in self.goal:
                print("You only need one")
            elif "Fist Full of Straws" in self.inventory and "Dirty Potato Sack" in self.inventory:
                self.inventory.remove("Fist Full of Straws")
                self.inventory.remove("Dirty Potato Sack")
                self.goal.append("Straw Bed")
                print("You have crafted Straw Bed")
            else:
                print("You do not have the crafting material")
        elif choice == "3":
            if "Small Hut" in self.goal:
                print("You only need one")
            elif all(item in self.inventory for item in ["Crumbling Stones","Rusty Umbrella","Rope"]):
                self.inventory.remove("Crumbling Stones")
                self.inventory.remove("Rusty Umbrella")
                self.inventory.remove("Rope")
                self.goal.append("Small Hut")
                print("You have crafted Small Hut")
            else:
                print("You do not have the crafting material")
        else:
            print("Invalid choice")