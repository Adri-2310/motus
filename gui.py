import ttkbootstrap as ttk

def screen_init(title: str):
    """
    Initialize the main window of the application with a given title.

    Args:
        title (str): The title of the window.
    """
    root = ttk.Window(themename='superhero')
    root.title(title)
    root.place_window_center()
    screen_widget(root)
    return root

def create_quadrillage(columns_size: str, canvas: ttk.Canvas):
    """
    Create a grid on the given canvas.

    Args:
        columns_size (str): The number of columns for the grid.
        canvas (ttk.Canvas): The canvas on which to draw the grid.
    """
    canvas.delete("grid")
    canvas.config(width=50 * int(columns_size), height=30 * 10)
    for line in range(10):
        for columns in range(int(columns_size)):
            y0 = line * 50
            x0 = columns * 50
            y1 = (line + 1) * 50
            x1 = (columns + 1) * 50
            canvas.create_rectangle(x0, y0, x1, y1, fill="gray")

def play_game(columns_size, canvas: ttk.Canvas):
    """
    Play the game by creating a grid on the canvas.

    Args:
        columns_size: The number of columns for the grid.
        canvas (ttk.Canvas): The canvas on which to draw the grid.
    """
    print(columns_size)
    create_quadrillage(columns_size, canvas)

def replay_game():
    """
    Reset the game to replay.
    """
    pass

def to_do_validate():
    """
    Validate the user's input.
    """
    pass

def screen_widget(root: ttk.Window):
    """
    Create and organize widgets on the main window.

    Args:
        root (ttk.Window): The main window on which to add the widgets.
    """
    # Create styles for widgets
    style_play = ttk.Style()
    style_play.configure("Play.TButton", background="#80e680", font=("Helvetica", 12))
    style_replay = ttk.Style()
    style_replay.configure("Replay.TButton", background="#0089d7", font=("Helvetica", 12))
    style_quit = ttk.Style()
    style_quit.configure("Quit.TButton", background="#f4aeae", font=("Helvetica", 12))
    style_valid = ttk.Style()
    style_valid.configure("Valid.TButton", background="#80e680", font=("Helvetica", 12))
    style_frame = ttk.Style()
    style_frame.configure(style="Frame.TFrame", background="gray")

    # Create a frame for top widgets
    frame_top = ttk.Frame(root)
    frame_top.pack(side="top", fill="x", expand=True)
    ttk.Label(frame_top, text="Timer").pack(side="left", padx=10, pady=2)
    spinbox_timer = ttk.Spinbox(frame_top, from_=0, to=100, width=5)
    spinbox_timer.pack(side="left")
    spinbox_timer.insert(0, "45")
    ttk.Label(frame_top, text="s.").pack(side="left")
    spinbox_letter = ttk.Spinbox(frame_top, from_=0, to=100, width=5)
    spinbox_letter.pack(side="left", padx=10, pady=2)
    spinbox_letter.insert(0, "6")
    ttk.Label(frame_top, text="lettres").pack(side="left")
    ttk.Button(frame_top, text="Jouer", command=lambda: play_game(spinbox_letter.get(), board), style="Play.TButton").pack(side="right")

    # Create a frame for letter entry
    frame_entry_letter = ttk.Frame(root, style="Frame.TFrame")
    frame_entry_letter.pack(side="top", fill="x", expand=True)
    entry_letter = ttk.Entry(frame_entry_letter)
    entry_letter.pack(fill="both")

    # Create a frame for the validate button
    frame_button_validate = ttk.Frame(root)
    frame_button_validate.pack(side="top", fill="both", expand=True)
    ttk.Button(frame_button_validate, text="Valider", command=to_do_validate, style="Valid.TButton").pack(fill="both", anchor="center")

    # Create a frame for the clock label
    frame_label_clock = ttk.Frame(root)
    frame_label_clock.pack(side="top", fill="both", expand=True)
    ttk.Label(frame_label_clock, text="0", anchor="center").pack(fill="both", anchor="center")

    # Create a frame for the game board
    frame_board = ttk.Frame(root)
    frame_board.pack(side="top", fill="both", expand=True)
    board = ttk.Canvas(frame_board, background="white")
    board.pack(fill="both", expand=True, anchor="center")

    # Create a frame for the solution label
    frame_label_solution = ttk.Frame(root)
    frame_label_solution.pack(side="top", fill="both", expand=True)
    ttk.Label(root, text="Label", anchor="center").pack(fill="both")

    # Create widgets for the bottom frame
    frame_bottom = ttk.Frame(root, padding=10)
    frame_bottom.pack(side="top", fill="both", expand=True)
    ttk.Button(frame_bottom, text="Rejouer", command=replay_game, style="Replay.TButton").pack(fill="both", side="left", expand=True)
    ttk.Button(frame_bottom, text="Quitter", command=root.destroy, style="Quit.TButton").pack(fill="both", side="right", expand=True)
