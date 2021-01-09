import random
import turtle as t


def get_line_length():
    choice = input('Enter line lenth(long, medium, short): ')
    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length = 100
    return line_length



def get_line_width():
    choice = input('Enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 25
    else:
        line_width = 10
    return line_width


def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside


line_length = get_line_length()
line_width = get_line_width()


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)