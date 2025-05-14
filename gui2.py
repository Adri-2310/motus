import ttkbootstrap as tk


def action_go():
    pass


def action_clear():
    pass


def screen_init(title : str):
    root = tk.Window(themename='superhero')
    root.title(title)
    root.place_window_center()

    btn_go = tk.Button(root, text="go", command=lambda: action_go())
    btn_go.pack(side="left",padx=10,pady=10)
    btn_clear = tk.Button(root, text="clear", command=lambda: action_clear())
    btn_clear.pack(side="right",padx=10,pady=10)
    board = tk.Canvas(root, background="white",height=500,width=500)
    board.pack(side="bottom")

    board.delete("grid")
    columns_size = 6
    board.config(width=50*columns_size, height=500*10)
    for line in range(10):
        for columns in range(columns_size):
            y0 = line * 50
            x0 = columns * 50
            y1 = (line + 1) + 500
            x1 = (columns + 1) + 500
            board.create_rectangle(x0, y0, x1, y1, fill="blue")


    return root
if __name__ == '__main__':
    screen_init("test").mainloop()