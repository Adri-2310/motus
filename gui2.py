import ttkbootstrap as tk


def action_go():
    pass


def action_clear():
    pass


def screen_init(title : str):
    root = tk.Window(themename='superhero')
    root.title(title)
    root.place_window_center()

    btn_go : tk.Button = tk.Button(root, text="go", command=lambda: action_go())
    btn_go.pack(side="left",padx=10,pady=10)
    btn_clear : tk.Button = tk.Button(root, text="clear", command=lambda: action_clear())
    btn_clear.pack(side="right",padx=10,pady=10)
    board : tk.Canvas = tk.Canvas(root, background="white")
    board.pack(side="bottom",fill="both",expand=True)
    root.mainloop()


if __name__ == '__main__':
    screen_init("test")