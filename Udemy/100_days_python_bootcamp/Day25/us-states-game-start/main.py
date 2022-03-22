# day 25 of 100
# U.S. states game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
turtle.addshape(image)          # adding the picture location as the new shape


turtle.shape(image)             # making the U.S. map as the background of the screen
answer_state = screen.textinput(title="Guess the state", prompt="What's another state?").title()
data = pandas.read_csv("50_states.csv")

mqo = turtle.Turtle()
guessed_states = []
states_to_learn = []
all_states = data.state.tolist()  # This converts the dataframe to a python list

while len(guessed_states) < 50:
    if answer_state == "Exit":   # adding all the states not mentioned in a states to learn list
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        break
    if answer_state in data.values:
        guessed_states.append(answer_state)
        state_xcor = int(data[data.state == answer_state].x)    # retrieving the x coordinate from dataframe
        state_ycor = int(data[data.state == answer_state].y)
        location = (state_xcor, state_ycor)
        mqo.penup()
        mqo.hideturtle()
        mqo.color("black")
        mqo.goto(location)
        mqo.write(answer_state, move=True, align="center", font=('Arial', 8, 'normal'))
    if len(guessed_states) > 0:
        prompt = "What's another state?"
        answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt=prompt)).title()

df = pandas.DataFrame(states_to_learn)      # convert the list to a dataframe
df.to_csv("states_to_learn.csv")  # use dataframe function to write its' data on a csv file

turtle.mainloop()               # this keeps the screen on until the user wants to close it
