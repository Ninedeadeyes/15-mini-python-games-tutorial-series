import os
import random


turn=True
game=True
counter=0
goal=0

numberlist1=[0,7]
numberlist2=[1,2]

while game:
     os.system('cls')
     counter=0
     goal=0
     print("                       Who Dares Win            "             )
     print("                                                     ")
     print("The aim of the game is to roll the dice as many times as possible, ")
     print("without the total going over 21. Each successful roll you will gain 5 points")
     print("There will be a selection of dices to choose from. ")
     print(" Will you acquire the highest score ?")
     print("                                                     ")
     with open("high.txt", "r") as f:
         old_score = f.read()
         print("The highest score is ",old_score)
         high_score=int(old_score)

     with open("name.txt", "r") as r:
         old_name = r.read()
         print("by ",old_name)
     print("                                                     ")

     while goal <21:
          while turn:
               decide=input("Pick dice(1,2,3 or 4)")


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
                    bob=random.randint(2,4)
                    counter-=bob
                    print("You lose ", bob, " points")
                    break
                    
               else:
                    print ("Wrong choice")

              
          
          input("press enter to roll dice" )
          print("you rolled a",dice)
          goal+=dice
          print("The total is ",goal)
          counter+=5
          again=input("keep playing? Y/N")
          again=again.upper()

          if again==("N"):
               break

          else:
               pass
          
     if goal>21:
          print("Sorry you went over 21")
          input("Press enter to exit")
          break


     else:
                    
          new_score=counter
          print("You score",new_score)

          if new_score >high_score:
               print("Congratulations,you have got the highest score !! ")
               New_name=input( " Enter your name :")
               best_name=open("name.txt",'w')
               best_name.write(New_name)
               best_name.close()

               new_score=str(new_score)
               best_score=open("high.txt",'w')
               best_score.write(new_score)
               best_score.close()
               
               print("The new highest score is", new_score)
               print("by : ",New_name)
               again=input("play again? Y/N")
               again=again.upper()

               if again == ("Y"):
                   pass

               else:
                   input("Press enter to exit")
                   break
         
               

          else:
              print("You did not beat the previous highest score of", high_score, "by ",old_name)
              again=input("play again? Y/N")
              again=again.upper()

              if again == ("Y"):
                  pass

              else:
                    input("Press enter to exit")
                    break
         
         
#https://github.com/Ninedeadeyes/15-mini-python-games-
