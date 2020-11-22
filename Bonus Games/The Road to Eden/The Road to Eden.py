print("                    The Road to Eden                     ")
print("You and your men are on an urgent mission to get to City of Eden")
print("to deliver an important message. Will you get there on time? ")
print("                     ")

file= open ("info.txt","r")     # This will open up the text file and r = read mode 
line=file.readline()            # This will read each line of your text and then the next 
Info=line.split("#")            # This will split the line/list by each # eg: Info[0],Info[1] 

Match=[]                        # An empty list



while Info[0]!= "END":               
    print(Info[0])
    print("       ")
    print(Info[1])
    print("       ")
    guess=input("(A or B): ")
    guess=guess.upper()


    if guess == "A":
        Match.append(Info[2])
        line=file.readline()
        Info=line.split("#")

    elif guess=="B":
        Match.append(Info[3])
        line=file.readline()
        Info=line.split("#")

    else:
        guess=input("Number not allowed,try again ")
                         

hard=Match.count("H")   # Add up the number of 'H' eg if there is 3xH, hard=3

soft=Match.count("S")

evil=Match.count("E")



if evil==1:
    print ("Even though you reach Eden, you are quickly arrested for crimes against humanity ")

elif hard > soft:
    print ("Even though you reach Eden, your crew abandons you for being too cruel")

elif soft > hard:
    print ("You fail to reach Eden. You wasted too much time along the way")

elif soft==hard:
    print ("Congratulations, you reach Eden on time. Your men celebrate your victory")

    
 #https://github.com/Ninedeadeyes/15-mini-python-games-



    

