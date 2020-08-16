import tkinter as tk
import random


class Snake(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        my_frame = tk.Frame(parent)

        coords_label_dict = {}
        board_len = 20  # size of the edge of a board
        refresh_time = 100  # in milliseconds. Time taken by snake to move his head to another square

        position = [board_len-1, int((board_len-1)/2)]
        direction = "top"
        snake_tail = [position]
        snake_last_fragment = "none"
        food_timer = 0
        food_list = []
        game_over = False
        scoreboard = tk.Label(my_frame, text="Score: 1", font=("Helvetica", 16, "bold"))

        black_image = tk.PhotoImage(file="black_16x16.png")
        green_image = tk.PhotoImage(file="green_16x16.png")
        dark_green_image = tk.PhotoImage(file="dark_green_16x16.png")
        red_image = tk.PhotoImage(file="red_16x16.png")

        def reset_game(event):
            nonlocal position
            nonlocal direction
            nonlocal snake_tail
            nonlocal snake_last_fragment
            nonlocal food_timer
            nonlocal food_list
            nonlocal game_over
            nonlocal scoreboard

            position = [board_len - 1, int((board_len - 1) / 2)]
            direction = "top"
            snake_tail = [position]
            snake_last_fragment = "none"
            food_timer = 0
            food_list = []
            game_over = False
            scoreboard = tk.Label(my_frame, text="Score: 0", font=("Helvetica", 16, "bold"))

            construct_board()
            update_board()

        def top_direction(event):
            nonlocal direction
            if direction != "bot":
                direction = "top"

        def bot_direction(event):
            nonlocal direction
            if direction != "top":
                direction = "bot"

        def left_direction(event):
            nonlocal direction
            if direction != "right":
                direction = "left"

        def right_direction(event):
            nonlocal direction
            if direction != "left":
                direction = "right"

        def get_food_coords():
            x = random.randint(0, board_len-1)
            y = random.randint(0, board_len-1)

            return x, y

        def get_coords_of_snake_fragment():
            nonlocal position

            x, y = position

            if x > 0 and direction == "top":
                x = x - 1

            if x < board_len - 1 and direction == "bot":
                x = x + 1

            if y > 0 and direction == "left":
                y = y - 1

            if y < board_len - 1 and direction == "right":
                y = y + 1

            position = (x, y)
            coords_of_snake_fragment = tuple(position)
            return coords_of_snake_fragment

        def get_coords_of_snake(old_snake_coords):
            nonlocal snake_last_fragment
            nonlocal snake_tail
            nonlocal game_over

            new_snake_coords = []
            new_snake_fragment = get_coords_of_snake_fragment()

            print("old snake coords", old_snake_coords)
            print("new snake fragment", new_snake_fragment)

            if new_snake_fragment in old_snake_coords:
                game_over = True

            if not game_over:
                new_snake_coords = old_snake_coords
                new_snake_coords.append(new_snake_fragment)
                if new_snake_fragment not in food_list:  # snake is not extending
                    snake_last_fragment = new_snake_coords.pop(0)
                snake_tail = new_snake_coords

            return new_snake_coords

        def draw_snake(snake_coords):
            for element in snake_coords:
                if snake_coords.index(element) == len(snake_coords)-1:  # coloring snake head in dark green
                    img = dark_green_image
                else:  # coloring the rest of snake tail in normal green
                    img = green_image
                snake_square = coords_label_dict[tuple(element)]
                snake_square.config(image=img)
                snake_square.grid(row=element[0], column=element[1])

            coords_label_dict[tuple(snake_last_fragment)].config(image=black_image)

        def update_board():
            nonlocal food_timer

            snake_coords_list = get_coords_of_snake(snake_tail)
            draw_snake(snake_coords_list)

            food_timer = food_timer + 1
            if food_timer in range(0, 100000000, 20):
                food_coords = get_food_coords()
                while food_coords in snake_coords_list:
                    food_coords = get_food_coords()
                food_list.append(food_coords)
                coords_label_dict[food_coords].config(image=red_image)  # draw food

            score = len(snake_tail)
            score_txt = " Score: " + str(score)
            scoreboard.config(text=score_txt)
            scoreboard.grid(row=board_len + 1, column=0, columnspan=7)

            # print(" ")
            # print("snake tail", snake_tail)
            # print("snake_last_fragment", snake_last_fragment)
            # print("food list", food_list)
            # print(" ")

            if not game_over:
                root.after(refresh_time, update_board)

        def construct_board():
            for x in range(0, board_len):
                for y in range(0, board_len):
                    square = tk.Label(my_frame, image=black_image, borderwidth=0, highlightthickness=0)
                    coords_label_dict[(x, y)] = square
                    coords_label_dict[(x, y)].grid(row=x, column=y)

            advice_label = tk.Label(my_frame, text="Press Space (only once) to restart")
            advice_label.grid(row=board_len + 1, column=6, columnspan=15)

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

        my_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('SNAKE')
    Snake(root).pack()
    root.mainloop()
