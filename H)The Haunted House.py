

def showInstructions():
    print('''


                    The Haunted House

Escape the house with its riches but beware of the evil undead !!  


Commands:

  use [item] eg: use key 
  
  shoot[monster] eg: shoot zombie
   
  go [direction] eg: go south
  
  get [item] eg: get bandage

''')
    
health= 100

def showStatus():

  print('You are in the ' + currentRoom)
  print (rooms[currentRoom]['desc'])
  print("Inventory : " + str(inventory))
  print("Your health is",health)
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


    
inventory = []

monster=[]

rooms = {

            'Hall' : {'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  "north":"Bed Room",
                  'item'  : 'shotgun',
                  'monster'  : '', "desc":"No one has been here for a while",
                },        

            'Kitchen' : { 'north' : 'Hall',
                  "item":"golden_crown",
                  'monster'  : 'zombie',"desc":"Dead bodies scatter the floor",                        
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'key',
                  'monster'  : 'zombie',"desc":"Old painting hangs on the wall",    
                },
                
            'Garden' : { 'north' : 'Dining Room',
            'monster'  : '', "desc": "There is a locked gate here",
                },

        'Bed Room' : {'south' : 'Hall',
            'item'  : 'bandage',
            'monster'  : 'ghoul',"desc":"There is blood all over the bed ",  
              },        
         }

# Nested Dictionary 

currentRoom = 'Hall'

showInstructions()

while True:

  showStatus()                  # Everytime it refresh it will show you up to date status 

  move = ''
  while move == '':  
    move = input('>')           # If you click enter with no command it will just ask for input  
    
  move = move.lower().split()   # lower case everything and split will turn a string into a list hence  ' get shotgun' = move =[get,shotgun]

  if move[0]=="shoot":    # acquire the value from index 0 of the list of 'move'. In this case if it is shoot  
      if "monster"in rooms[currentRoom] and move[1] in rooms[currentRoom]['monster'] and "shotgun" in inventory :
          del rooms[currentRoom]['monster']
          print( "you killed the", move[1])
          rooms[currentRoom].update({"monster":"dead"},)  #update merge dictionary with an iterable of key value pair
        
      else:
          print("you cannot attack " )
          

      
  if move[0]=="use":
      
      
      if "bandage" in inventory and move[1]== "bandage":
          heal=40
          health=min(100,health+heal)
          inventory.remove("bandage")
          print("you recovered 40 health (max 100)")

      elif "key" in inventory and move[1]== "key" and "golden_crown" in inventory and currentRoom=="Garden":     
         print("you escape with the loot, you retire in style, you win!!  ")
         break    
              
          
      elif "key" in inventory and move[1]== "key" in inventory and currentRoom=="Garden":
         print("you escape the house but die a pauper, you lose ")
         break

      

      else:
          print("can't use that")

      
    
  if move[0] == 'go':
      if move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]    # acquire the new room (the value) from the 'direction'(the nested key) 
                                                       #eg rooms[Dining room][west] return value Hall hence currentRoom=Hall
      else:
          print('You can\'t go that way!')

  if move[0] == 'get' :
          
      if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          inventory += [move[1]]
          print(move[1] + ' got!')
          del rooms[currentRoom]['item']
     
      else:
          print("Can\'t get that")
        
  if 'zombie' in rooms[currentRoom]['monster']:
      print("A zombie attack you !!!")
      health=health-30

  if 'ghoul' in rooms[currentRoom]['monster']:
      print('A ghoul attack you !!!')
      health=health-20
  

  if health <= 0:
      print("you are dead")
      break
