cure=False
goblin =False
quest1=False
potion=False



print ("                    The King's Curse              ")
print (" Art by eVil, Glory Moon, Dustin Slater and Joan Stark     ")
print 
print ("""  

       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'



""")




Name=input("What is your name brave adventurer ? ")

print("Hello "+Name)

print("Someone has turned the King into stone. Your Quest is to remove the curse !!!")

while cure==False:

    print("                                    ")
    print("Where do you want to go ? (A,B,C or D ")
    print ("A) Castle  B) The Old Hags Hut  C) The Wild Forest  D) Fortress of Doom")
    Choice=input()
    Choice=Choice.lower()


    if Choice=="a":

        print ("""

                                -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )






              """)

        if potion==True:

            cure=True
            
        else:
            print("You go back to the castle with empty hands.")
            


    if Choice=="b":

        print("""


        /^\ 
       // \\    ,@@@@@@@,
      //   \\ ,@@@\@@@@/@@,
     // === \\ @@\@@@/@@@@@
    // =-=-= \\@@@@\@@@@@@;%
   //   ===   \\@@@@@@/@@@%%%,
  //|         |\\@\\//@@%%%%%%
  ~ |         | ~ @|| %\\//%%%
    |  __ __  |    || %%||%%'
    | |  |  | |    ||   ||
    | | -|- | |    ||   ||
    |_|__|__|_|    ||   ||
  /`  =======  `\__||_._||
/`    =======            `\





""")

        if quest1==True and goblin ==True:
            print("The old hag thank you for your help and wish you the best in your quest.")

        if quest1==False and goblin ==True:

                print("As you approach the old hag's hut, you see an old hag smiling at you. ")
                print("she thank you for saving her pet goblin and is willing to help your quest.")
                print("she tells you that there is a magical potion in the Fortress of Doom. ")
                print("It will cure the King. She provides you with a map and the location.  ")
                print("Before you leave she informs you of the fortress password 'DARKSTONE'")
                quest1=True

        if quest1 == False and goblin == False:
            print("As you approach the old hag's hut, an army of crows chase you away.")

    if Choice=="c":
        print("You enter the wild forest....")

        print("""

           * *    
           *    *  *
      *  *    *     *  *
     *     *    *  *    *
 * *   *    *    *    *   *
 *     *  *    * * .#  *   *
 *   *     * #.  .# *   *
  *     "#.  #: #" * *    *
 *   * * "#. ##"       *
   *       "###
             "##
              ##.
              .##:
              :###
              ;###
            ,####.
/\/\/\/\/\/.######.\/\/\/\/\         


""")

        if goblin==False:
            print ("You see a goblin trapped in some bramble do you help (YES OR NO) ")
            Help=input()
            Help.lower()

            if Help=="yes"or Help=="YES":
                print ("You help the goblin, the goblin runs back home.")
                goblin=True


        else:
            print("You see nothing of importance here, maybe you will go hunting later")


    if Choice=="d":

        print("""

           `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_\_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_\_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_\_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_\_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_\_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
                         //=========\\



""")
        if quest1==True and potion == False:

            while potion ==False:
                print("You stand at the entrance of the Fortress of Doom.")
                print("You hear a booming voice.. 'Halt, what is the password ?")
                Answer=input()
                Answer=Answer.lower()

                if Answer=="darkstone":
                    print("They allow you into the Fortress and you quickly locate the magical potion.")
                    potion=True


                else:

                    print(" INCORRECT !! NOW FEAR MY POWER !! ")
                    print("A great fireball consumes your body and ends your adventure")
                    print("                   GAME OVER                   ")
                    print ("""


            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    


                           """)


                    print("Press any button to exit the game")
                    input()
                    exit()
                    
                    
        else:
            print("You arrive at the Fortress of Doom but with no purpose, you quickly leave.")


print("You pour the magical potion over the King's stone body.")
print("It has worked, the curse is removed.")
print("You are rewarded with 10,000 gold !!! ")
print("                                       ")
print ("             GAME OVER                      ")
print("                                       ")            
print("                                       ")        

print("""

             
           (_)
          .-'-.
          |   |
          |   |
          |   |
          |   |
        __|   |__   .-.
     .-'  |   |  `-:   :
    :     `---'     :-'
     `-._       _.-'
         '""""""

""")


input("press enter to exit")
            
        

        

    

    
    
    
