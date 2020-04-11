import turtle
import random
import time 

# set up screen 

turtle.ht()
turtle.setup(950,950)
turtle.title("Space Rescue")
turtle.bgcolor("black")

#This saves memory
turtle.setundobuffer(0)
#This speeds up drawing
turtle.tracer(0)



class Game():
    def __init__(self):                     # All class will have a method __init__ which provide instructions on what arguments is needed, example below
        self.pen = turtle.Turtle()          # Has also invoked an turtle method (an additional attribute) to draw borders. 
        
    def draw_border(self):  #Function that draw border         
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-400, 400)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(800)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()



class Pen(turtle.Turtle):              # Example of class inheritance, inheriting from the parent 'turtle.Turtle' 
    def __init__(self):
        super().__init__()             # alternative can be turtle.Turtle.__init__(self)
                                       # instead of super(),will let the parent class to       
    def show_rules(self):              # handle additional attributes/function.
        self.ht()                      # This is needed to inherit turtle.Turtle classes/methods. 
        self.up()
        msg = ("Controls: ArrowKeys, Rescue the red ships and avoid the rocks  ")
        self.goto(-300, -450)
        self.color("white")
        self.write(msg, font=("Arial", 16, "normal"))
        self.pendown()
        self.penup()


    def you_lose(self):
        self.ht()
        self.up()
        self.goto(-170,450)
        self.color("white")
        msg = ("""
        You lose, final points:%s""") %(player1.points)       
        self.write(msg, font=("Arial", 16, "normal"))


    def show_points1(self):
        self.ht()
        self.up()
        self.goto(310,450)
        self.color("white")
        msg = " Points:%s" %(player1.points)        
        self.write(msg, font=("Arial", 16, "normal"))
    
    def update_points1(self):
        self.undo()
        self.ht()
        self.up()
        self.goto(310,450)
        self.color("white")
        msg = "Points:%s" %(player1.points)        
        self.write(msg, font=("Arial", 16, "normal"))


class Sprite(turtle.Turtle):

    def __init__(self, shape, color, startx, starty):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        
                                     #Boundary detection
        if self.xcor() > 390:
            self.setx(390)
            self.rt(135)
        
        if self.xcor() < -390:
            self.setx(-390)
            self.rt (135)
        
        if self.ycor() > 390:
            self.sety(390)
            self.rt (135)
        
        if self.ycor() < -390:
            self.sety(-390)
            self.rt (135)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

    def destroy(self):
        self.goto(9000,9000)
        self.hideturtle()


class Player(Sprite):
    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)   # Because of super() we don't need
        self.speed =1                                          # write out those attributes again 
        self.points=0                                          # eg : self.color within player class. 
                                                               # Since it will be handles by parent class 
    def turn_left(self):                                       # Any difference will need to be alter eg: self.speed
        self.lt(45)
        
        
    def turn_right(self):
        self.rt(45)
       

    def accelerate(self):
        if self.speed==2:
            pass
        else:
            self.speed += 1 
        
    def decelerate(self):
        if self.speed == -1:
            pass
        else:
            self.speed -= 1
            

class Ship(Sprite):
    def __init__(self, shape, color, startx, starty):
        super().__init__(shape, color, startx, starty)
        self.speed = 0
        self.setheading(random.randint(0,360))

        
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__(spriteshape, color, startx, starty)
        self.speed = .5
        self.setheading(random.randint(0,360))

game = Game()  #call game function 

game.draw_border()  # draw border 


player1 = Player(("triangle"),"blue",-380,-380)

turtle.onkey(player1.turn_left, "Left")
turtle.onkey(player1.turn_right, "Right")
turtle.onkey(player1.accelerate, "Up")
turtle.onkey(player1.decelerate, "Down")


turtle.listen()

points1=Pen()
points1.show_points1()
rules=Pen()
rules.show_rules()


ship=[]
    
for shi in range(3):
    ship.append(Ship("circle","red",random.randint(-370,370),random.randint(-370,370)))


maxenemies= random.randint(10,16)

enemies =[]
for i in range(maxenemies):
    enemies.append(Enemy("square", "grey",0, 0))
    enemies[i].setposition(random.randint(-300,300),random.randint(-300,300))


#Game loop
while True:
    player1.move()

    for enemy in enemies:
        enemy.move()

        if player1.is_collision(enemy):
                player1.destroy()
                points1.you_lose()
                for enemy in enemies:
                    enemy.speed=0
                time.sleep(5)
                break
            



    for shi in range (3):
        if player1.is_collision(ship[shi]):
           x = random.randint(-390, 390)
           y = random.randint(-390, 390)
           ship[shi].goto(x, y)
           player1.points+=100
           points1.update_points1()


    turtle.update()


# __init__ Example



#class Computer():
#    def __init__(self, computer, ram, ssd):
#        self.computer = computer
#        self.ram = ram
#        self.ssd = ssd
#        print ("Computer info is below ")
#
#
#lenovo = Computer('lenovo', 2, 512)
#print('This computer is:', lenovo.computer)
#print('This computer has ram of', lenovo.ram)
#print('This computer has ssd of', lenovo.ssd)
#
#  
#Computer info is below 
#This computer is: lenovo
#This computer has ram of 2
#This computer has ssd of 512
 





    
