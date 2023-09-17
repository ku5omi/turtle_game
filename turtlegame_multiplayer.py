# Turtle Graphics Game

import turtle
import math
import random
import os
import time

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(3)
wn.bgpic("kbgame-bg.gif")

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
player.color("palevioletred")
player.shape("turtle")
player.penup()
player.speed(0)

# Create player 2 turtle
player2 = turtle.Turtle()
player2.color("yellow")
player2.shape("turtle")
player2.penup()
player2.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition score
mypen2 = turtle.Turtle()
mypen2.color("red")
mypen2.hideturtle()

# Create variable score
score = 0
score2 = 0

# Create food
maxFoods = 10
foods = []
for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.shapesize(0.5)
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

# Set speed variable
speed = 1.8
speed2 = 1.8

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 60


# Define functions for first player
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


# Define functions for second player
def turn_left_p2():
    player2.left(30)


def turn_right_p2():
    player2.right(30)


def increase_speed_p2():
    global speed2
    speed2 += 1


def isCollision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 20:
        return True
    else:
        return False


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")

# **Keyboard binding for second player**
turtle.onkey(turn_left_p2, "a")
turtle.onkey(turn_right_p2, "d")
turtle.onkey(increase_speed_p2, "w")

while True:
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1
    player.forward(speed)
    player2.forward(speed2)
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Comp Checking x coordinate
    if player2.xcor() > 290 or player2.xcor() < -290:
        player2.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Comp Checking y coordinate
    if player2.ycor() > 290 or player2.ycor() < -290:
        player2.right(180)
        os.system("afplay bounce.mp3&")

    # Move food around
    for food in foods:
        food.forward(3)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            os.system("afplay bounce.mp3&")

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            os.system("afplay bounce.mp3&")

        # Collision checking player
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system("afplay chomp.mp3&")
            score += 1
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" % score
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # Collision checking comp
        if isCollision(player2, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system("afplay chomp.mp3&")
            score2 += 1
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(260, 310)
            scorestring2 = "Score: %s" % score2
            mypen.write(scorestring2, False, align="left", font=("Arial", 14, "normal"))
if int(score) > int(score2):
    mypen.setposition(0, 0)
    mypen.color("green")
    mypen.write(
        "Game Over: Player 1 WINS", False, align="center", font=("Arial", 28, "normal")
    )
else:
    mypen.setposition(0, 0)
    mypen.color("red")
    mypen.write(
        "Game Over: Player 2 WINS", False, align="center", font=("Arial", 28, "normal")
    )
delay = input("Press Enter to finish.")
