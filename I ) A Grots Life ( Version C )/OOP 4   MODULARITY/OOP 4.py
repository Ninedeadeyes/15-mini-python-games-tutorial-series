# I have put the main() def into its own class and renamed it play()

'''
Within the code 

Encapsulation (bundling data and methods together, and controlling access to internal state.) is demonstrated by 

1) Private method __pass_time: by prefixing with __, you’ve made it “hidden” from outside use. Only the goblin itself can advance time — that’s encapsulation.

2) Attributes inside classes: Hunger, health, inventory, and gold are stored inside the Goblin object. They aren’t floating around as global variables — they’re encapsulated within the goblin.

Abstraction (means hiding complex details and exposing only what’s necessary to use an object.)  is demonstrated by 

1) Goblin class: You don’t need to know how hunger increases or health decreases internally — you just call gob.eat(), gob.hunt(), or gob.rest().

2) Game class: The player interacts with simple menu choices (1 - Status, 2 - Eat, etc.), while the underlying logic (random loot, damage calculation, inventory management) is abstracted away inside methods.


'''
from game_data import GameData
from character import Goblin


class Game:
    def __init__(self):
        gob_name = input("What do you want to name your Goblin?: ")
        self.data = GameData()
        self.gob = Goblin(gob_name, 0, 100, 0, 20, self.data)
        self.endgame = False

    def play(self):
        choice = None  
        while choice != "0":
            print(f"\nSo... {self.gob.name}, what is your action?")
            print("""
            0 - Quit
            1 - Status
            2 - Eat
            3 - Scavenge 
            4 - Explore
            5 - Rest
            6 - Craft 
            """)
    
            choice = input("Choice: ")

            if choice == "0":
                print("Good-bye.")
            elif choice == "1":
                self.gob.status()
            elif choice == "2":
                self.gob.eat()
            elif choice == "3":
                self.gob.farm()
            elif choice == "4":
                self.gob.hunt()
            elif choice == "5":
                self.gob.rest()
            elif choice == "6":
                self.gob.craft()
            else:
                print("Invalid choice.")

            if self.gob.hunger > 20:
                print("Died from hunger")
                break
            if self.gob.health <= 0:
                print("Died from wounds")
                break

            if not self.endgame and all(goal in self.data.goal for goal in ["Fish Bone Spear","Straw Bed","Small Hut"]):
                print("You have built your home and proved you are a survivor, you win!!")
                con = input("Do you want to continue playing 1-yes, 2-no: ")
                if con == "1":
                    self.endgame = True
                elif con == "2":
                    print("Good bye")
                    break

if __name__ == "__main__":
    Game().play()