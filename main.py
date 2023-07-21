import turtle
import pandas
screen = turtle.Screen()
screen.title("State of united states")
image = "india-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv")

# for finding the x and y core
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

all_states = data.state.to_list()
print(all_states)
guess_state = []

while len(guess_state) < 30:
    answer_text = screen.textinput(f"{len(guess_state)}/30 guess", "Another State?").title() # title to convert string to title
    if answer_text == "Exit":
        missing_state =[]
        for state in all_states:
            if state not in guess_state:
                missing_state.append(state)
        # this code will create a csv file for states which you have not guessed
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_no_guess.csv")
        break
    if answer_text in all_states:
        guess_state.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_text)

# This Code will Create a csv file for states which you have guessed correct
df = pandas.DataFrame(guess_state)
df.to_csv("guess_list.csv")


