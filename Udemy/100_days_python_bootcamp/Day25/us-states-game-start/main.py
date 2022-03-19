import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)
answer_state = screen.textinput(title="Guess the state", prompt="What's another state?").title()
data = pandas.read_csv("50_states.csv")

score = 0
guess = 0

while guess < 50:
    for state in data:
        if state["state"] == answer_state:
            score += 1
            state_xcor = state["x"]
            state_ycor = state["y"]
            state_location = (state_xcor, state_ycor)
            turtle.write(answer_state, move=False, align=state_location, font=('Arial', 8, 'normal'))
    guess += 1

turtle.mainloop()
