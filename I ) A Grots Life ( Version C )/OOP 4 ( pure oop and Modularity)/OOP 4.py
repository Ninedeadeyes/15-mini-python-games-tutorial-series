
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