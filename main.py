import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your Bet", prompt="Which Turtle will win the race choices (red/ green/ orange/ blue/ purple/ black)? Enter a color: ")
colors = ["red", "green", "orange", "blue", "purple", "black"]
y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!!")
            else:
                print(f"You have Lost!! The {winning_color} won the race ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
