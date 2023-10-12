from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.shape('turtle')
t.color('red')


def move_forward():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.left(15)


def turn_right():
    t.right(15)


def clear_screen():
    t.clear()


s.listen()
s.onkeypress(key='w', fun=move_forward)
s.onkeypress(key='s', fun=move_backwards)
s.onkeypress(key='a', fun=turn_left)
s.onkeypress(key='d', fun=turn_right)
s.onkey(key='c', fun=clear_screen)


s.exitonclick()
