import tkinter as tk


class Snake(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        my_frame = tk.Frame(parent)

        board_len = 20
        coords_label_dict = {}
        black_image = tk.PhotoImage(file="black_16x16.png")
        green_image = tk.PhotoImage(file="green_16x16.png")
        snake_was_there = []
        position = [10, 10]
        direction = ["none"]

        def get_top_direction(event):
            direction.clear()
            direction.append("top")

        def get_bot_direction(event):
            direction.clear()
            direction.append("bot")

        def get_left_direction(event):
            direction.clear()
            direction.append("left")

        def get_right_direction(event):
            direction.clear()
            direction.append("right")

        def get_snake_coords():
            x, y = position

            if x > 0:
                if direction[0] == "top":
                    x = x - 1
            if x < board_len - 1:
                if direction[0] == "bot":
                    x = x + 1
            if y > 0:
                if direction[0] == "left":
                    y = y - 1
            if y < board_len - 1:
                if direction[0] == "right":
                    y = y + 1

            position[0] = x
            position[1] = y

            snake_coords = tuple(position)
            return snake_coords

        def draw_snake(coords):
            nonlocal snake_was_there

            snake_square = coords_label_dict[coords]
            snake_square.config(image=green_image)
            snake_square.grid(row=coords[0], column=coords[1])

            if len(snake_was_there) != 0:
                coords_label_dict[snake_was_there[0]].config(image=black_image)
                print("coords", coords, "snake was there", snake_was_there[0])

            snake_was_there.clear()
            snake_was_there.append(coords)

        def update_board():
            snake_coords = get_snake_coords()
            draw_snake(snake_coords)
            root.after(100, update_board)

        def construct_board():
            for x in range(0, board_len):
                for y in range(0, board_len):
                    square = tk.Label(my_frame, image=black_image, borderwidth=0, highlightthickness=0)
                    square.image = black_image
                    coords_label_dict[(x, y)] = square
                    coords_label_dict[(x, y)].grid(row=x, column=y)

        my_frame.focus_set()
        my_frame.bind("<w>", get_top_direction)
        my_frame.bind("<s>", get_bot_direction)
        my_frame.bind("<a>", get_left_direction)
        my_frame.bind("<d>", get_right_direction)

        construct_board()
        update_board()
        my_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('SNAKE')
    Snake(root).pack()
    root.mainloop()
