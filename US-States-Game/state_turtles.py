from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 12, 'normal')


class StateTurtle(Turtle):

    def __init__(self, cord_tuple, state_name):
        super().__init__()
        self.penup()
        self.ht()
        self.state_name = state_name
        self.cord_tuple = cord_tuple
        self.add_state()

    def add_state(self):
        self.goto(self.cord_tuple)
        self.write(self.state_name, align=ALIGNMENT, font=FONT)
# Take the coords and write the name of the state on those cords