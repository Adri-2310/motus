import ttkbootstrap as ttk

def screen_init(title : str, size : str,):
    root = ttk.Window(themename='superhero')
    root.title(title)
    root.geometry(size)
    root.place_window_center()

    # configure grid root
    root.columnconfigure(0, weight=1)
    root.rowconfigure(4, weight=1)

    screen_widget(root)
    return root


def play_game():
    pass


def replay_game():
    pass


def to_do_validate():
    pass


def screen_widget(window:ttk.Window):
    # frame
    frame_top = ttk.Frame(window)
    frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    frame_bottom = ttk.Frame(window, padding=10)

    #create sytle for widgets
    style_play = ttk.Style()
    style_play.configure("Play.TButton",background="#80e680" ,font=("Helvetica", 12))
    style_replay = ttk.Style()
    style_replay.configure("Replay.TButton",background="#0089d7" ,font=("Helvetica", 12))
    style_quit = ttk.Style()
    style_quit.configure("Quit.TButton",background="#f4aeae" ,font=("Helvetica", 12))
    style_valid = ttk.Style()
    style_valid.configure("Valid.TButton",background="#80e680" ,font=("Helvetica", 12))

    # create widgets top frame
    ttk.Label(frame_top,text="Timer").pack(side="left",padx=10,pady=2)
    ttk.Spinbox(frame_top, from_=0, to=100,width=5).pack(side="left",padx=10,pady=2)
    ttk.Label(frame_top,text="s.").pack(side="left")
    ttk.Spinbox(frame_top, from_=0, to=100,width=5).pack(side="left",padx=10,pady=2)
    ttk.Label(frame_top,text="lettres").pack(side="left",padx=10,pady=2)
    ttk.Button(frame_top,text="Jouer",command=play_game,style="Play.TButton").pack(side="right",padx=10,pady=2)

    # creat widgets bottom frame
    ttk.Button(frame_bottom,text="Rejouer",command=replay_game,style="Replay.TButton").pack(side="left",expand=True)
    ttk.Button(frame_bottom,text="Quitter",command=window.destroy,style="Quit.TButton").pack(side="right",expand=True)

    # input
    ttk.Entry(window).grid(row=1, column=0, sticky="ew",padx=10,pady=10)
    ttk.Button(window, text="Valider", command=to_do_validate,style="Valid.TButton").grid(row=2, column=0, sticky="ew",padx=10,pady=10)
    ttk.Label(window, text="0",anchor="center").grid(row=3, column=0,sticky="ew",padx=10,pady=10)
    ttk.Canvas(window,background="white").grid(row=4, column=0, sticky="nsew",padx=10,pady=10)
    ttk.Label(window, text="Label",anchor="center").grid(row=5, column=0,sticky="ew",padx=10,pady=10)
    frame_bottom.grid(row=6, column=0, sticky="ew",padx=10,pady=10)

