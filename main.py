import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()




data = pandas.read_csv("50_states.csv")

correct_guesses = []
while len(correct_guesses)<50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # for state in data.state:
        #     if state not in correct_guesses:
        #         missed_states.append(state)
        missed_states = [state for state in data.state if state not in correct_guesses]
        df = pandas.DataFrame(missed_states)
        df.to_csv("learn.csv")


        break

    for state in data.state:
        if state == answer_state:
            x = int(data.x[data.state == answer_state])
            y = int(data.y[data.state == answer_state])
            cursor.goto(x, y)
            cursor.write(answer_state,align= "center", font=("Courier", 10, "normal"))
            correct_guesses.append(answer_state)





