# Turtle Graphics Game - Kuromi-Inspired Slash

import turtle

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor("black")

# Create player turtle
player = turtle.Turtle()
player.color("darkorchid")
player.shape("turtle")
player.pendown()

# Set speed variable
speed = 1
while True:
    player.forward(speed)
