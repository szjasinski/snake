from tkinter import *
import random

root = Tk()
root.title('SNAKE')


my_frame = Frame(root, width=500, height=500, highlightbackground="black")
my_frame.pack(fill=BOTH, expand=1)

COORDS_SQUARE_DICT = {}
N = 20  # size of the edge of a board
REFRESH_TIME = 100  # in miliseconds. Time between snake moves

COUNTER = [N-1, int((N-1)/2)]
DIRECTION = "top"
SNAKE_TAIL = [COUNTER]
SNAKE_LAST_SQUARE = "none"
FOOD_TIMER = 0
FOOD_LIST = []
GAME_OVER = False
SCOREBOARD = Label(my_frame, text="Score: 0", font=("Helvetica", 16, "bold"))

black_image = PhotoImage(file="black_16x16.png")
green_image = PhotoImage(file="green_16x16.png")
dark_green_image = PhotoImage(file="dark_green_16x16.png")
red_image = PhotoImage(file="red_16x16.png")


def reset_game(event):
    global COUNTER
    global DIRECTION
    global SNAKE_TAIL
    global SNAKE_LAST_SQUARE
    global FOOD_TIMER
    global FOOD_LIST
    global GAME_OVER
    global SCOREBOARD

    COUNTER = [N - 1, int((N - 1) / 2)]
    DIRECTION = "top"
    SNAKE_TAIL = [COUNTER]
    SNAKE_LAST_SQUARE = "none"
    FOOD_TIMER = 0
    FOOD_LIST = []
    GAME_OVER = False
    SCOREBOARD = Label(my_frame, text="Score: 0", font=("Helvetica", 16, "bold"))

    construct_board()
    update_board()


def top_direction(event):
    global DIRECTION
    if DIRECTION != "bot":
        DIRECTION = "top"


def bot_direction(event):
    global DIRECTION
    if DIRECTION != "top":
        DIRECTION = "bot"


def left_direction(event):
    global DIRECTION
    if DIRECTION != "right":
        DIRECTION = "left"
    print(DIRECTION)


def right_direction(event):
    global DIRECTION
    if DIRECTION != "left":
        DIRECTION = "right"


def get_food_coords():
    x = random.randint(0, N-1)
    y = random.randint(0, N-1)

    return x, y


def get_coords_of_snake_fragment():
    global COUNTER

    x = COUNTER[0]
    y = COUNTER[1]

    if x > 0 and DIRECTION == "top":
        x = x - 1

    if x < N - 1 and DIRECTION == "bot":
        x = x + 1

    if y > 0 and DIRECTION == "left":
        y = y - 1

    if y < N - 1 and DIRECTION == "right":
        y = y + 1

    COUNTER = (x, y)
    coords_of_snake_fragment = tuple(COUNTER)

    return coords_of_snake_fragment


def get_coords_of_snake(old_snake_coords):
    global SNAKE_LAST_SQUARE
    global SNAKE_TAIL
    global GAME_OVER
    new_snake_coords = []
    new_snake_fragment = get_coords_of_snake_fragment()

    print("old snake coords", old_snake_coords)
    print("new snake fragment", new_snake_fragment)

    for element in old_snake_coords:
        if element == new_snake_fragment:
            GAME_OVER = True

    if not GAME_OVER:
        is_snake_extending = False
        for element in FOOD_LIST:
            if element == new_snake_fragment:
                is_snake_extending = True
        if is_snake_extending:
            new_snake_coords = old_snake_coords
            new_snake_coords.append(new_snake_fragment)
        else:
            new_snake_coords = old_snake_coords
            new_snake_coords.append(new_snake_fragment)
            SNAKE_LAST_SQUARE = new_snake_coords.pop(0)
        SNAKE_TAIL = new_snake_coords

    return new_snake_coords


def draw_snake(snake_coords, snake_last_square):
    global COORDS_SQUARE_DICT

    for element in snake_coords:
        if snake_coords.index(element) == len(snake_coords)-1:  # coloring snake head in darker green
            img = dark_green_image
        else:
            img = green_image
        snake_square = COORDS_SQUARE_DICT[tuple(element)]
        snake_square.config(image=img)
        snake_square.grid(row=element[0], column=element[1])

    COORDS_SQUARE_DICT[tuple(snake_last_square)].config(image=black_image)


def draw_food(food_coords):
    global COORDS_SQUARE_DICT
    COORDS_SQUARE_DICT[food_coords].config(image=red_image)


def update_board():
    global COUNTER
    global FOOD_TIMER
    global SCOREBOARD

    snake_coords_list = get_coords_of_snake(SNAKE_TAIL)
    draw_snake(snake_coords_list, SNAKE_LAST_SQUARE)

    FOOD_TIMER = FOOD_TIMER + 1
    if FOOD_TIMER in range(0, 100000000, 20):
        food_coords = get_food_coords()
        while food_coords in snake_coords_list:
            food_coords = get_food_coords()
        FOOD_LIST.append(food_coords)
        draw_food(food_coords)

    score = len(SNAKE_TAIL)
    score_txt = " Score: " + str(score)
    SCOREBOARD.config(text=score_txt)
    SCOREBOARD.grid(row=N + 1, column=0, columnspan=7)

    # print(" ")
    # print("snake tail", SNAKE_TAIL)
    # print("snake_last_square", SNAKE_LAST_SQUARE)
    # print("food list", FOOD_LIST)
    # print(" ")

    if not GAME_OVER:
        root.after(REFRESH_TIME, update_board)


def construct_board():

    for x in range(0, N):
        for y in range(0, N):
            square = Label(my_frame, image=black_image, borderwidth=0, highlightthickness=0)
            COORDS_SQUARE_DICT[(x, y)] = square
            COORDS_SQUARE_DICT[(x, y)].grid(row=x, column=y)

    advice_label = Label(my_frame, text="Press Space to reset")
    advice_label.grid(row=N + 1, column=8, columnspan=10)


construct_board()
update_board()

root.focus_set()

root.bind("<w>", top_direction)
root.bind("<s>", bot_direction)
root.bind("<a>", left_direction)
root.bind("<d>", right_direction)

root.bind("<Up>", top_direction)
root.bind("<Down>", bot_direction)
root.bind("<Left>", left_direction)
root.bind("<Right>", right_direction)

root.bind("<space>", reset_game)


root.mainloop()
