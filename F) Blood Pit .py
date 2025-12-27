hero_max_power=[20]
hero_max_health=[300]
hero_health=[300]        # This is a list [] with only one item
hero_power=[20]
turn_counter=1
rep=[0]

"""
Technically you can just use one list to represent each of the stats but it will look much more confusing 

hero_stats-[20,300,300,20,0]
0= hero_max_power 1= hero_max_health  2=hero_health 3=hero_power 4=rep  etc 

So the first 'enemy function' would be 

def enemy(name,enemy_hp,enemy_pow):
    print(f"{name} {enemy_hp}hp {enemy_pow} power")
    while hero_stats[2]>0 and enemy_hp>0:
        hero_stats[2]-=enemy_pow
        enemy_hp-=hero_stats[3]
        print(f"The {name} attacks you. Your health is {hero_stats[2]}")
        print(f"You attack the {name}. The {name}'s health is {enemy_hp}")
        
        if hero_stats[2]<=0:
            print("hero has been slained") 
            input("Press enter to quit")
            quit()
        
        if enemy_hp<=0:
            print("You have slained the "+name)
            break

"""

def enemy(name,enemy_hp,enemy_pow):
    print(f"{name} {enemy_hp}hp {enemy_pow} power")
    while hero_health[0]>0 and enemy_hp>0:
        hero_health[0]-=enemy_pow
        enemy_hp-=hero_power[0]
        print(f"The {name} attacks you. Your health is {hero_health[0]}")
        print(f"You attack the {name}. The {name}'s health is {enemy_hp}")
        
        if hero_health[0]<=0:
            print("hero has been slained") 
            input("Press enter to quit")
            quit()
        
        if enemy_hp<=0:
            print("You have slained the "+name)
            break

def level_up(hp_increase,pow_increase,enemy,rep_points):
     rep[0]+=rep_points
     hero_max_health[0]+=hp_increase
     hero_max_power[0]+=pow_increase
     hero_health[0] = hero_max_health[0] 
     hero_power[0] = hero_max_power[0] 
    
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
            level_up(30,10,"Goblin",10)
            break
            
        elif choose==("ORC"):
            enemy("Orc",400,60)
            level_up(50,15,"Orc",50)
            break
        
        elif choose==("PIT FIGHTER"):
            enemy("Pit Fighter",500,200)
            level_up(70,25,"Pit Fighter",100)
            break

        elif choose==("RED DRAGON"):
            enemy("Red Dragon",1500,400)
            level_up(100,30,"Red Dragon",300)
            break
            
        else:
            print("Try again")
            break

    turn_counter+=1
    print(f"It is turn {turn_counter}")  # no need to change an integer to a string anymore 

    if rep[0]>2500:
        print("You are the master of the blood pit")
        print(f"You beat the game on turn {turn_counter}")
        input("You win, press enter to exit")
        break 

#https://github.com/Ninedeadeyes/15-mini-python-games-
   


    
    
