import turtle
from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_over = False

states_data = pandas.read_csv("50_states.csv")

pen = Turtle()
pen.penup()
pen.hideturtle()

while game_over == False:

    user_answer = (screen.textinput(title="Guess the State", prompt="Name a state in the USA")).title().strip()


    if user_answer in states_data.state.values:

        row = states_data[states_data.state == user_answer]
        x_cor = row.x.iloc[0]
        y_cor = row.y.iloc[0]
        pen.goto(x_cor, y_cor)

        pen.write(user_answer, align=ALIGNMENT, font=FONT)





turtle.mainloop()