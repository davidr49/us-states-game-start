import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game_is_on = True
guessed_states = []

while len(guessed_states) < 50:

    remaining_states = 0
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct.", prompt="What's another state's "
                                                                                              "name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for answers in data["state"]:
        if answers in answer_state:
            guessed_states.append(answer_state)
            state_answered = data[data.state == answers]
            x_coord = int(state_answered.x)
            y_coord = int(state_answered.y)
            new_state = turtle.Turtle()
            new_state.penup()
            new_state.hideturtle()
            new_state.goto(x_coord, y_coord)
            new_state.write(answer_state, align="center")



