from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

colors = ["blue", "yellow", "green", "red", "orange", "purple"]

prompt = "Which turtle will win the race?\nChoose one: blue, green, yellow, purple, orange, red"
user_choice = screen.textinput(title="Make your bet", prompt=prompt)

while user_choice is None or user_choice.strip().lower() not in colors:
    user_choice = screen.textinput(title="Invalid choice!",
        prompt="That's not a valid color. Please choose one of:\nblue, green, yellow, purple, orange, red")

user_choice = user_choice.strip().lower()

y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -210, y= y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"you've won! the {winning_color} is the winner.")
            else:
                print(f"you've lost! the {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()