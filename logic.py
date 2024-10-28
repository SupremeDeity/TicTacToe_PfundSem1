from tkinter import messagebox

cells = {}
turn = "X"
ended=False

def setTurnLabel(label):
    global turnLabel
    turnLabel = label
    turnLabel['text'] = "Turn: " + turn
def setWindow(win):
    global window
    window = win

def fillCell(row, col, button):
    cells.update({(row, col): button})
    
def updateCellState(row, col):
    global turn
    cells[(row, col)]['text']=turn
    cells[(row, col)]['state']="disabled"
    checkCondition()
    if not ended:
        if(turn == "X"):
            turn = "O"
        else:
            turn = "X"
        global turnLabel
        turnLabel['text']= "Turn: " + turn

def endGame(val):
    global window
    global turnLabel
    global ended
    ended=True
    turnLabel['text']=val
    turnLabel['font']=("", 18)
    turnLabel['foreground']="Red"
    for x in cells.values():
        x['state']="disabled"
    messagebox.showinfo("GAME OVER", val + "\nPress OK to close....")
    window.after_idle(lambda: window.destroy())

winning_combinations = [
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], # Diagonal 1,2
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], # ROW 1, 2, 3
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], # COL 1, 2, 3
]

def checkCondition():
    for combination in winning_combinations:
        if all(cells[index]['text'] == turn for index in combination):
            endGame(f"{turn} won")
    
    # moves exhausted -> DRAW
    if all(x['text'] != "" for x in cells.values()):
        endGame(f"GAME DRAW")