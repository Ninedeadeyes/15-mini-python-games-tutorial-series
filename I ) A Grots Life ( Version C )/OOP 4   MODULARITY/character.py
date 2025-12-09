import random

class Goblin:
    def __init__(self, name, hunger, health, provision, gold, data):       
        self.name = name                                         
        self.hunger = hunger
        self.health = health
        self.provision = provision
        self.gold = gold
        self.data = data

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
        print("You have", self.provision, "provisions")
        print("You have", self.data.inventory, "in your bag")
        print("You have", self.gold, "gold")
        print("You are", self.hung)
        print("You are", self.wounded)
        self.__pass_time()

    def eat(self, eat=5):     
        if self.hunger <= 0:
            print("You are not hungry")
        elif self.provision > 0 and self.data.larder:
            meal = random.choice(self.data.larder)
            print("You eat some", meal)
            self.data.larder.remove(meal)
            print("It was a tasty meal")
            self.hunger -= eat
            self.provision -= 2
        else:
            print("You do not have any food")
        self.__pass_time()
      
    def hunt(self):
        loot = random.choice(self.data.lootlist)
        enemy = random.choice(self.data.enemylist)
        
        if "Fish Bone Spear" in self.data.goal:
            print("Armed with your Fish Bone Spear...")
            damage = random.randint(1,10)
        else:
            damage = random.randint(11,30)
        self.health -= damage
            
        print("You came across a", enemy)
        print("After an epic fight you took", damage, "damage")         

        if loot in self.data.inventory:
            print("You see nothing of interest")
        else:
            self.data.inventory.append(loot)
            print("But you find", loot)

        coin = random.randint(1,5)
        self.gold += coin
        print("You have gained", coin, "gold")
        self.__pass_time()
        
    def farm(self, stash=2):
        grub = random.choice(self.data.food)
        print("You have found some", grub)
        self.data.larder.append(grub)
        print("You have gained", stash, "provisions")
        self.provision += stash
        self.__pass_time()
      
    def rest(self):
        if self.health >= 100:
            print("You do not need rest")
        else:
            if "Straw Bed" in self.data.goal:
                print("You rest better in your Straw Bed")
                sleep = random.randint(10,30)
            else:
                print("Sleeping on the floor is rough")
                sleep = random.randint(5,20)
            before = self.health
            self.health += sleep
            if self.health > 100:
                self.health = 100
            print("You have recovered", self.health - before, "health")
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
            if "Fish Bone Spear" in self.data.goal:
                print("You only need one")
            elif "Fish Bone" in self.data.inventory and "Old Stick" in self.data.inventory:
                self.data.inventory.remove("Fish Bone")
                self.data.inventory.remove("Old Stick")
                self.data.goal.append("Fish Bone Spear")
                print("You have crafted the Fish Bone Spear")
            else:
                print("You do not have the crafting material")
        elif choice == "2":
            if "Straw Bed" in self.data.goal:
                print("You only need one")
            elif "Fist Full of Straws" in self.data.inventory and "Dirty Potato Sack" in self.data.inventory:
                self.data.inventory.remove("Fist Full of Straws")
                self.data.inventory.remove("Dirty Potato Sack")
                self.data.goal.append("Straw Bed")
                print("You have crafted Straw Bed")
            else:
                print("You do not have the crafting material")
        elif choice == "3":
            if "Small Hut" in self.data.goal:
                print("You only need one")
            elif all(item in self.data.inventory for item in ["Crumbling Stones","Rusty Umbrella","Rope"]):
                self.data.inventory.remove("Crumbling Stones")
                self.data.inventory.remove("Rusty Umbrella")
                self.data.inventory.remove("Rope")
                self.data.goal.append("Small Hut")
                print("You have crafted Small Hut")
            else:
                print("You do not have the crafting material")
        else:
            print("Invalid choice")