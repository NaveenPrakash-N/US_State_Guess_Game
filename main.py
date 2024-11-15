import turtle
import pandas

screen = turtle.Screen()
screen.title("US Guess Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

class Write(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def add(self, name, x, y):
        self.goto(x, y)
        self.write(name)

guessed_states = []
answer_state = screen.textinput(title="Guess The State", prompt="Enter State Name").title()
game_is_on = True
guess = 1

while game_is_on and len(guessed_states) < 50:
    if answer_state in data["state"].values and answer_state not in guessed_states:
        row_data = data[data.state == answer_state]
        x, y = int(row_data["x"].iloc[0]), int(row_data["y"].iloc[0])
        writer = Write()
        writer.add(answer_state, x, y)
        guessed_states.append(answer_state)  # Add guessed state to the list
        if len(guessed_states) == 50:
            game_is_on = False
        else:
            answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt="Guess another state").title()
    else:
        answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt="Guess another state").title()

turtle.mainloop()
