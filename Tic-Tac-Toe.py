import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")
root.resizable(False, False)

board = [""] * 9
buttons = []
current_player = "X"

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return "" not in board

def computer_move():
    available = [i for i in range(9) if board[i] == ""]
    if available:
        move = random.choice(available)
        board[move] = "O"
        buttons[move].config(text="O", state="disabled", fg="red")

def on_click(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled", fg="blue")

        if check_winner("X"):
            status_label.config(text="🎉 You Win!")
            disable_all()
            return
        elif is_draw():
            status_label.config(text="It's a Draw!")
            return

        computer_move()

        if check_winner("O"):
            status_label.config(text="💻 Computer Wins!")
            disable_all()
        elif is_draw():
            status_label.config(text="It's a Draw!")

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global board
    board = [""] * 9
    status_label.config(text="Your Turn (X)")
    for btn in buttons:
        btn.config(text="", state="normal")

# Create buttons
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 12))
status_label.pack(pady=10)

reset_btn = tk.Button(root, text="Restart Game", command=reset_game)
reset_btn.pack()

root.mainloop()