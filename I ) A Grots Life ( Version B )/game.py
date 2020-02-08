import turtle
from goblin import Goblin   # Example of importing class (import all functions)
import time 



# A grots life. 

            
def main():    
    
    print( "                A Grot's Life By T.K  ")
    print("")
    time.sleep(1)

    print("You open your eyes and take your first breath ")
    time.sleep(1)
    print("You hear a voice in the darkness...")
    time.sleep(1)
    print("What is your name, you filthy Grot? ")
    gob_name = input("Name:")
    print(gob_name,".. it suits you. Now, go do what grots do..")
    time.sleep(1)
    print( "Kill, eat, sleep and get precious shinies !!  ")
    time.sleep(1)
    print("And maybe a place where your grubby face can call home")
    time.sleep(2)      
    gob = Goblin(gob_name,0,100,0,20)
    print("""
   .    .  .    .  .    .  .    .  .    .  .    .  .   .  .      
     .      @%%@     .       .   . @%%@    X  .      . .  .  
   .   . .  @::8@t;::::;::;::::.:@S;::@  .X.X;   .       .  .
     .     .tt%X :S%tXSStXStX%8S@tt8X::  X .;X.   . .  .     
   .    .   . .;88S:;;8@8X@8XX::;8... . X.::; X.          .  
      .   .   .   8:.         8:8.     X:::;;: X   .  . .    .
   .    .         8:.         @.8:  . X::.:;::::X    .    .   
     .     . . .  8:.         @.8.         :@    .    .   .  
   .   .  .      .8.:         S.8..    ..; :@      .    .   .
     .       .  . 8::         @.8:      .: :@ . .    .    .  
   .    .  .. :.tt8.::::::::::::Xt%t...  ..;@     .    .     
      .   ::.;X:.::t%%%%%%t%tS;tt:::X;X: . :@.  .   .    .  .
   .    . S;;@@::8t:;:;:;:;:;t:;8::t8S:t  .:@     .   .      
     .  ;X8S@8;8.8: .    .      8;;. ;X;t .;@. .    .   . .  
   .   XXS8%  ;@.8.   .    . .  8;:    @ 8:;@    .          .
      :XXS    :@.8.     .       8;..   . 8:;@ .    .  . .    
   .  X;;@  . ;@.8: . .   .  .  8;: .     .;@   .    .    .  
    .         ;@.:SXXXXXXXXXXXXX@:.   .   .:@ .   .     .   .
        . . . ;X..::........::.......     .;@   .   .  .     
 .   .         XXS:::@X@@XXS.;8X@X@S  .  . ;8     .      . . 
      .  .  .   .8;:..   . .;%   .  .   . .;@ .      .       
   .    .     .  8;.      ..t%        .  ..;@   .  .   .  .  
   .      SS%S@X@8;: . .  . X ; 8XSS     . :@ .  .   .   .  .
 .    .   8888888S    ...  888888888     . :@      .   .     
       . .     .     .        .  .   . .     .  .        .  
  . .       .     .   .       .   .              
  
  """)
    endgame= False
    choice = None  
    while choice != "0":
        #os.system("cls")   
       
        
        print("")
        print (  "  So... "  ,gob_name, " What is your action ?" )
        print \
        ("""
    
        0 - Quit
        1 - Status
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
            gob.explore()
          
        elif choice == "5":
            gob.rest()

        elif choice == "6":
            gob.craft()
            
        else:

            print("\nSorry, but", choice, "isn't a valid choice.")

        if gob.hunger >20:
            print("You have gone too many days without food. You have died from hunger")
            input("press any button to continue")
            break

        if gob.health <=0:
            print("You have suffered too many wounds, you have bled to death")
            input("press any button to continue")
            break

        if endgame == False:
            if ("Fish Bone Spear") in gob.goal and ("Straw Bed")in gob.goal and("Small Hut") in gob.goal:
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
