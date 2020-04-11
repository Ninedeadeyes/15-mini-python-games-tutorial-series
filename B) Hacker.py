

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

   if attempt == 8:
       print("too many attempts")
       input("press enter to quit")
       quit()

   raw = input("Enter the Password ")

   password=raw.lower()     
       
   
print("Access granted")
   

input("press enter to exit")  # In theory you can click any button to exit 


      # Examples of Python operators  
      
      #!= is not equal 
      # += add
      # -= minus
      # == equals
      # > Greater than
      # < less than
      # >= Greater than or equal to
      # <= Less than or equal to 
      
