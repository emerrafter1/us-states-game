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
all_states = states_data.state.to_list()

correct_guesses = []
number_of_states = len(all_states)

while (len(correct_guesses)/number_of_states) != 1:


    user_answer = (screen.textinput(title=f"{len(correct_guesses)}/{number_of_states} States Correct", prompt="Name a state in the USA")).title().strip()

    if user_answer == "Exit":

        states_to_learn = [state for state in all_states if state not in correct_guesses]

        states_to_learn_df = pandas.DataFrame({"States to learn": states_to_learn})
        states_to_learn_df.to_csv("states_to_learn.csv")
        break


    if user_answer in all_states and user_answer not in correct_guesses:
        t = Turtle()
        t.penup()
        t.hideturtle()
        row = states_data[states_data.state == user_answer]
        t.goto(row.x.item(), row.y.item())
        t.write(user_answer)
        correct_guesses.append(user_answer)

