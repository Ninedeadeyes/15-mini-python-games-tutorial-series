print("You are a hacker and attempting to hack Robert's bank account")
print("                                                                   ")
input("                 press enter to continue")
print("                                                                   ")
print("You know he is 24 years old and like cats and work as an accountant")
print("                                                                   ")

input("                 press enter to continue")
    
print ("Welcome to Catwest Security System")

raw = input("Enter the Password ")  

password=raw.lower()    # any input typed will become lower case 
                        # 'lower' is an in-built method 
attempt=0

while password != 'bob':    # When password is 'bob' this will break 
   print("Access denied")   # the while loop and then the next line 
   attempt+=1               # of code will play eg: print ("Access granted")
   

   if attempt == 1:
      print(" Tip(It has 3 letters)")

   if attempt == 3:
      print(" Tip(Begins with a 'B')")

   if attempt == 5:
      print(" Tip( Relates to his name)")

   if attempt == 7:
      print(" Tip( Ends with a 'B')")

   if attempt == 8:
       break

   raw = input("Enter the Password ")

   password=raw.lower()     
       
if attempt !=8:
   print("Access granted")
   input("press enter to exit")  # In theory you can click any button to exit 

else:
   print("too many attempts")
   input("press enter to quit")

#Variables 

# A variable is a container for storing data values. It is like a box to store something 
# example :  attempt=0 is a variable. The variable 'attempt' stores how many times you attempted the password.  
# raw is also a variable that is attached to the inbuilt function 'input' which means anything you type when it request 
# the password it will store it into 'raw'. 

# While loop 

# Python while loop is used to run a block code until a certain condition is met.
# In the below example while password is not 'bob' it will keep playing the looping until
# either password is 'bob' or on the 8th attempt with the 'break' keyword which will break 
# the loop

# Conditional Statements

# else statement 

#An else statement contains the block of code that executes 
#if the conditional expression in the if or ELIF statement resolves to 0 or a FALSE value


      # Examples of Python operators  
      
      #!= is not equal 
      # += add
      # -= minus
      # == equals
      # > Greater than
      # < less than
      # >= Greater than or equal to
      # <= Less than or equal to 
      
    #https://github.com/Ninedeadeyes/15-mini-python-games-

