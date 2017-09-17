import turtle
import os

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space Invaders")

# setup border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#creat player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

Playerspeed= 15

#creat enemey
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.position(-200, 250)

enemyspeed = 2

#Move Player left or right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#Move Player left or right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#creat Keybord bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")


#Main game loop
    while True:

        #Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.set(x)

        #Move the enemy back and down
        if enemy.cor() > 280:
            enemyspeed *= -1
        if enemy.xcor() < -280:
            enemyspeed *= -1


delay = raw_input('press enter to finish')
