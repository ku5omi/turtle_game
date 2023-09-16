# Turtle Graphics Game - Kuromi-Inspired Slash

import turtle
import math
import random

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor("black")

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.color("darkorchid")
mypen.speed(0)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("darkorchid")
player.shape("turtle")
player.penup()
player.speed(0)

# Create food
food = turtle.Turtle()
food.color("lightgreen")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(-100, 100)

# Set speed variable
speed = 1


# Define functions
def turn_left():
    player.left(15)


def turn_right():
    player.right(15)


def increase_speed():
    global speed
    speed += 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
while True:
    player.forward(speed)
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
    # Collision checking
    if isCollision(player, food):
    food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    