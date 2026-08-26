
# Who Dares Win 

# A tactical dice game with a high score save function. Demonstrate how to OPEN/READ/WRITE TXT.FILES as well as an example of 'clear screen' function.


import random

turn=True
game=True
counter=0
total=0
numberlist1=[0,7]
numberlist2=[1,2]

while game:
     print("\033[H\033[J", end="")   # clear screen function 
     counter=0
     goal=0
     print("                       Who Dares Win            "             )
     print("                                                     ")
     print("The aim of the game is to roll the dice as many times as possible, ")
     print("without the total going over 30. Each successful roll you will gain 5 points")
     print("There will be a selection of dices to choose from. ")
     print(" Will you acquire the highest score ?")
     print("                                                     ")
     with open("high.txt", "r") as f:
         old_score = f.read()
         print(f"The highest score is {old_score}")
         high_score = int(old_score)

     with open("name.txt", "r") as r:
         old_name = r.read()
         print(f"by {old_name}")
         print("                                                      ")

     while total <30:
         while turn:
               decide=input("Pick dice(1,2,3 or 4) : ")

               if decide==("1"):
                    dice=random.randint(2,5)
                    break

               if decide==("2"):
                    dice=random.randint(1,6)
                    break

               if decide==("3"):
                    dice=random.choice(numberlist1)
                    break

               if decide==("4"):
                    dice=random.choice(numberlist2)
                    deduction=random.randint(2,4)
                    counter-=deduction
                    print(f"You lose {deduction} points")
                    break
                    
               else:
                    print ("Wrong choice")

         input("press enter to roll dice")
         print(f"you rolled a {dice}")
         total += dice
         print(f"The total is {total}")
         print("You gain 5 points for the dice roll !!")
         counter += 5
         print(f"You have {counter} points")
         again = input("keep playing? Y/N : ")
         again = again.upper()

         if again==("N"):
             break

         else:
             pass
          
     if total>30:
          print("Sorry your total is over 30")
          print("You lose !! :( ")
          input("Press enter to exit")
          break
          
     else:          
         new_score=counter
         print(f"You score {new_score}")

         if new_score >high_score:
             print("Congratulations,you have got the highest score !! ")
             New_name=input( " Enter your name :")
             best_name=open("name.txt",'w')
             best_name.write(New_name)
             best_name.close()

             new_score=str(new_score)
             best_score=open("high.txt",'w')
             best_score.write(f"{new_score}")
             best_score.close()
               
             print(f"The new highest score is {new_score}")
             print(f"by : {New_name}")

         else:
             print(
             f"You did not beat the previous highest score of {high_score} by"
             f" {old_name}")

         again=input("play again? Y/N : ")
         again=again.upper()

         if again == ("Y"):
             pass

         else:
             input("Press enter to exit")
             break
                   
#https://github.com/Ninedeadeyes/15-mini-python-games-