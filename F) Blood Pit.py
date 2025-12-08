
# with f string there is no need to change an integer into a string anymore 

hero_max_power=20
hero_max_health=300
hero_health=300        
hero_power=20
turn_counter=0
rep=0

def enemy(name,enemy_hp,enemy_pow):
    print(f"{name} {enemy_hp}hp {enemy_pow} power")
    eh=enemy_hp
    ep=enemy_pow  
    hh= hero_health          
    hp= hero_power         
    while hh>0 and eh>0:
        hh-=ep
        eh-=hp
        print(f"The {name} attacks you. Your health is {hh}")
        print(f"You attack the {name}. The {name}'s health is {eh}")
        
        if hh<=0:
            print("hero has been slained") 
            input("Press enter to quit")
            quit()
        
        if eh<=0:
            print("You have slained the "+name)
            break

def level_up(hp_increase,pow_increase,enemy,rep_points):
     global hero_max_health, hero_max_power, hero_health, hero_power, rep
     rep+=rep_points
     hero_max_health+=hp_increase
     hero_max_power+=pow_increase
     hero_health=hero_max_health
     hero_power=hero_max_power
     print(f"you become stronger with every {enemy} you slay")
     print("you gain some reputation for the fight")
     print( f"Totol Reputation: {rep}")   # no need to change an integer to a string anymore 
     
while True:
    print("Welcome to the blood pit, choose your opponent!! ")
    choose=input( "Please select goblin, orc, pit fighter or red dragon: ")
    choose=choose.upper()

    while choose in ("GOBLIN", "ORC", "PIT FIGHTER", "RED DRAGON"):
        print("your opponent is a...")

        if choose==("GOBLIN"):
            enemy("Goblin",200,20)
            level_up(20,5,"Goblin",10)
            break
            
        elif choose==("ORC"):
            enemy("Orc",400,60)
            level_up(40,10,"Orc",50)
            break
        
        elif choose==("PIT FIGHTER"):
            enemy("Pit Fighter",500,200)
            level_up(60,20,"Pit Fighter",100)
            break

        elif choose==("RED DRAGON"):
            enemy("Red Dragon",1500,400)
            level_up(70,30,"Red Dragon",200)
            rep+=200
            break
            
        else:
            print("Try again")
            break

    turn_counter+=1
    print(f"It is turn {turn_counter}")  # no need to change an integer to a string anymore 

    if rep>2000:
        print("You are the master of the blood pit")
        print(f"You beat the game in turn {turn_counter}")
        input("You win, press enter to exit")
        break 
    
#https://github.com/Ninedeadeyes/15-mini-python-games-
   