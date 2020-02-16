hero_max_power=20
hero_max_health=300
hero_health=[300]
hero_power=[20]
turn_counter=0
rep=0

def enemy(name,a,b):
    print(name+" "+str(a)+"hp "+str(b)+" power")
    health=a
    power=b  
    hh= hero_health[0]
    hp= hero_power[0]
    while hh>0 or health>0:

        (hh)-=(power)
        (health)-=(hp)
        print("The "+name+" attack you.Your health is "+str(hh))
        print("You attack the "+name+".The "+name+" health is "+ str(health))
        
        if hh<=0:
            print("hero has been slained") 
            input("Press enter to quit")
            quit()
        
        if health<=0:
            print("You have slained the "+name)
            break
        
            
        


while True:
    
    print("Welcome to the blood pit, choose your opponent!! ")
    choose1=input( "Please select goblin, orc, pit fighter or red dragon: ")
    choose=choose1.upper()

    while choose is "GOBLIN" or "ORC" or "PIT FIGHTER" or "RED DRAGON":

        if choose==("GOBLIN"):
            print("You fight")
            enemy("Goblin",200,20)
            rep+=10
            hero_max_health+=20
            hero_health[0]=hero_max_health
            hero_max_power+=5
            hero_power[0]=hero_max_power
            print("you become stronger with every goblin you slay")
            print("you gain some reputation for the fight")
            print("Totol Reputation: "+ str(rep))
            break
            


        elif choose==("ORC"):
            print("You fight")
            enemy("Orc",400,60)
            rep+=50
            hero_max_health+=40
            hero_health[0]=hero_max_health
            hero_max_power+=10
            hero_power[0]=hero_max_power      
            print("you become more powerful with every orc you crush")
            print("you gain some reputation for the fight")
            print("Totol Reputation: "+ str(rep))
            break
        

        elif choose==("PIT FIGHTER"):
            print("You fight")
            enemy("Pit Fighter",500,200)
            rep+=100
            hero_max_health+=60
            hero_health[0]=hero_max_health
            hero_max_power+=20
            hero_power[0]=hero_max_power       
            print("you gain experience for every pit fighter you battle")
            print("you gain some reputation for the fight")
            print("Totol Reputation: "+ str(rep))
            break

        elif choose==("RED DRAGON"):
            print("You fight")
            enemy("Red Dragon",1500,400)
            rep+=300
            hero_max_health+=70
            hero_health[0]=hero_max_health
            hero_max_power+=30
            hero_power[0]=hero_max_power
            print("You become more vicious for every red dragon you face")
            print("you gain some reputation for the fight")
            print("Totol Reputation: "+ str(rep))  
            
            break
            

        else:
            print("Try again")
            break

    turn_counter+=1
    print("It is turn "+str(turn_counter))

    if rep>2000:
        print("You are the master of the blood pit")
        print("You beat the game in turn "+ str(turn_counter))
        input("You win, press enter to exit")
        break 
    


    


   


    
    
