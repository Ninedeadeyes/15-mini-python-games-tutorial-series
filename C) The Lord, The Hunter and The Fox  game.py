import random
list1= ["fox","hunter","lord"]  

print("This is an alternative game of rock, paper and scissors ")
print("")
win_count=0
win=True

while win:
    cpu=random.choice(list1)
    user=input("Enter your choice:[fox, hunter, lord] or exit :  ")
    user=user.lower()
    
    if (user=="fox" and cpu=="lord")or(user=="hunter" and cpu=="fox")or (user=="lord" and cpu=="hunter"):
        print("computer choose " , cpu)
        print("You have won")
        win_count+=1
        
    elif (user=="lord" and cpu=="fox")or(user=="fox" and cpu=="hunter")or (user=="hunter" and cpu=="lord"):
        print("computer choose " , cpu)
        print("You lose")
       
    elif user=="exit":
        print("Goodbye")
        print("you won, ", win_count,"times")
        win=False
        
    elif user==cpu:
        print("computer choose " , cpu)
        print("It is a draw")

    elif user != ("fox") or ("hunter")or ("lord"):
        print("not valid")
        

       
