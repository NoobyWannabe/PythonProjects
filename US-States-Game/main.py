import turtle
import pandas as pd
from state_turtles import StateTurtle

screen = turtle.Screen()
screen.title('U. S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
# print(states_data.head(5))
all_states = data.state.to_list()
print(all_states)
# take the guess from the user:
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name? NOTE: type 'exit' to quit.").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        state_name = data[data.state == answer_state]
        state_name_x = int(state_name.x.item())
        state_name_y = int(state_name.y.item())
        cord_tuple = (state_name_x, state_name_y)
        st = StateTurtle(cord_tuple=cord_tuple, state_name=answer_state)
    else:
        print("that is not a valid state.")
    print(guessed_states)

# generate the states to learn.csv
states_to_learn = [state for state in all_states if state not in guessed_states]
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)


states_to_learn = pd.DataFrame(states_to_learn)
states_to_learn.to_csv("learn.csv")














screen.exitonclick()