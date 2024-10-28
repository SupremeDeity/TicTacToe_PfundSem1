import tkinter as tk # main class
from tkinter import ttk # themed tkinter

from logic import fillCell, setTurnLabel, setWindow, updateCellState

def game_start():
    ########## WINDOW SETTINGS START ##########
    # Initialize Tkinter
    window = tk.Tk()
    # Set title
    window.title("Tic Tac Toe")

    # Get screen size and width to center window
    scr_width = window.winfo_screenwidth()
    scr_height = window.winfo_screenheight()

    # window positioning variables
    win_width = 600
    win_height = 400
#     x = int(scr_width / 2 - win_width / 2)
#     y = int(scr_height / 2 - win_height / 2)

    # Set window size (widthxheight+x+y)
    window.geometry(f"{win_width}x{win_height}+{x}+{y}")
    # Prevent window from being resized
    window.resizable(False, False)
    ########## WINDOW SETTINGS END ##########

    ########## Main GUI SETUP START ##########
    detailsFrame = ttk.Frame(window)

    titleLabel = ttk.Label(detailsFrame, text="Tic Tac Toe", font=("" , 18))
    titleLabel.pack()

    turnLabel = ttk.Label(detailsFrame, font=("" , 16), foreground="Green")
    turnLabel.pack()

    detailsFrame.pack()

    gameFrame = ttk.Frame(window)

    ##### BUTTON CREATION START #####
    for row in range(3):
        for col in range(3):
            button = ttk.Button(gameFrame, command=lambda row=row, col=col: updateCellState(row, col))
            button.grid(row=row, column=col, ipady=20, padx=10, pady=10)
            fillCell(row, col, button)
    s = ttk.Style()
    s.configure('TButton', font=('', 20))
    gameFrame.pack()
    ##### BUTTON CREATION END #####

    # Pass state to logic
    setWindow(window)
    setTurnLabel(turnLabel)
    ########## Main GUI SETUP END ##########

    # Runs the main loop/reacts to changes
    window.mainloop()

game_start()