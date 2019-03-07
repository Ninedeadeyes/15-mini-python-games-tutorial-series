

print("You are a hacker and attempting to hack Robert's bank account")
input("                 press enter to continue")
print("                                                                   ")
print("You know he is 24 years old and like cats and work as an accountant")
print("                                                                   ")
input("                 press enter to continue")
    
print ("Welcome to Catwest Security System")



raw = input("Enter the Password ")

password=raw.lower()

attempt=0

while password != 'bob': 
   print("Access denied")
   attempt+=1
   

   if attempt == 1:
      print(" Tip(It has 3 letters)")

   if attempt == 3:
      print(" Tip(Begins with a 'B')")

   

   if attempt == 7:
       print("too many attempts")
       input("press enter to quit")
       quit()

   raw = input("Enter the Password ")

   password=raw.lower()
       
   
print("Access granted")
   

input("press enter to exit")



      #!= is not equal 
      # += add 
