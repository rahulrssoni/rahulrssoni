import time
import turtle
from turtle import Turtle
from random import randint

win = turtle.Screen()
win.title("turtle race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.goto(-140, 200)
turtle.write("turtle race",font=("Arial",30,"bold"))
turtle.penup()

turtle.goto(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()

track = turtle.Turtle()
track.hideturtle()
track.penup()
track.goto(-400, -180)
track.color("chocolate")
track.begin_fill()
track.pendown()
for _ in range(2):
    track.forward(800)
    track.right(90)
    track.forward(300)
    track.right(90)
track.end_fill()
colors = ["red", "blue", "yellow", "white", "black", "pink"]
turtles = []

y_pos = [-100, -70, -40, -10, 20, 50]

for i in range(6):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-380, y_pos[i])
    turtles.append(t)


turtles = []


winner = None   
while True:
    for t in turtles:
        for t in turtles:
            move = randint(1, 10)
            t.forward(move)

            if t.xcor() > 380:
                winner = t.pencolor()
                break
    if winner:
        break