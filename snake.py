from tkinter import *

root = Tk()
root.title('SNAKE')


my_frame = Frame(root, width=500, height=500, highlightbackground="black")
my_frame.pack(fill=BOTH, expand=1)

COORDS_SQUARE_DICT = {}
SNAKE_COORDS = (10, 10)
SNAKE_WAS_THERE = "x"
COUNTER = [10, 10]
DIRECTION = "none"
N = 20

black_image = PhotoImage(file="black_16x16.png")
green_image = PhotoImage(file="green_16x16.png")


def get_top_direction(event):
    global DIRECTION
    DIRECTION = "top"
    print(DIRECTION)


def get_bot_direction(event):
    global DIRECTION
    DIRECTION = "bot"
    print(DIRECTION)


def get_left_direction(event):
    global DIRECTION
    DIRECTION = "left"
    print(DIRECTION)


def get_right_direction(event):
    global DIRECTION
    DIRECTION = "right"
    print(DIRECTION)


def get_snake_coords():
    global COUNTER

    x = COUNTER[0]
    y = COUNTER[1]

    if x > 0:
        if DIRECTION == "top":
            x = x - 1
    if x < N-1:
        if DIRECTION == "bot":
            x = x + 1
    if y > 0:
        if DIRECTION == "left":
            y = y - 1
    if y < N-1:
        if DIRECTION == "right":
            y = y + 1

    COUNTER = (x, y)
    snake_coords = tuple(COUNTER)

    return snake_coords


def draw_snake(coords):
    global COORDS_SQUARE_DICT
    global SNAKE_WAS_THERE

    snake_square = COORDS_SQUARE_DICT[coords]
    snake_square.config(image=green_image)
    snake_square.grid(row=coords[0], column=coords[1])

    if SNAKE_WAS_THERE != "x":
        COORDS_SQUARE_DICT[SNAKE_WAS_THERE].config(image=black_image)

    SNAKE_WAS_THERE = coords
    print("coords", coords, "snake was there", SNAKE_WAS_THERE)


def update_board():
    global SNAKE_COORDS
    global COUNTER

    snake_coords = get_snake_coords()
    draw_snake(snake_coords)

    print(snake_coords)
    root.after(100, update_board)


def construct_board():
    for x in range(0, N):
        for y in range(0, N):
            square = Label(my_frame, image=black_image, borderwidth=0, highlightthickness=0)
            COORDS_SQUARE_DICT[(x, y)] = square
            COORDS_SQUARE_DICT[(x, y)].grid(row=x, column=y)


construct_board()
update_board()

root.focus_set()
root.bind("<w>", get_top_direction)
root.bind("<s>", get_bot_direction)
root.bind("<a>", get_left_direction)
root.bind("<d>", get_right_direction)


root.mainloop()
