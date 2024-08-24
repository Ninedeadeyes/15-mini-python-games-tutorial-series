import random

list1= ["fox","hunter","lord"]  

print("This is an alternative game of rock, paper and scissors ")
print("")
win_count=0
lose_count=0
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
        lose_count+=1

    elif user==cpu:
        print("computer choose " , cpu)
        print("It is a draw")

       
    elif user=="exit":
        print("Goodbye")
        print("you won, ", win_count,"times.", "You lose,",lose_count,"times.")
        win=False
        
    else:
        print("not valid")
        
# List 

# List is a Data Structure (a specialized format for organizing, processing, retrieving and storing data. )
# Lists are used to store multiple items in a single variable, eg :  list1= ["fox","hunter","lord"]  

# Conditional Statements

# elif statement 

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
# At the above example if it is none of the decisions it will try the condition 'else' 

#https://github.com/Ninedeadeyes/15-mini-python-games-

