from tkinter import *

root = Tk()
root.title('SNAKE')

# TESTING A COMMIT


def update_board():
    global SNAKE_COORDS
    global COUNTER

    snake_coords = get_snake_coords()
    draw_snake(snake_coords)

    print(snake_coords)
    root.after(100, update_board)


class Snake:

    N = 20
    coords_label_dict = {}
    black_image = PhotoImage(file="black_16x16.png")

    def __init__(self, master):
        for x in range(0, Snake.N):
            for y in range(0, Snake.N):
                square = Label(master, image=Snake.black_image, borderwidth=0, highlightthickness=0)
                Snake.coords_label_dict[(x, y)] = square
                Snake.coords_label_dict[(x, y)].grid(row=x, column=y)


s = Snake(root)

root.mainloop()