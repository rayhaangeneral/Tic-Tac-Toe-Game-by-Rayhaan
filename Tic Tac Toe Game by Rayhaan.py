import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.create_widgets()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Helvetica", 32),
                                   width=4, height=2, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def create_widgets(self):
        self.turn_label = tk.Label(self.master, text=f"Turn: {self.turn}",
                                   font=("Helvetica", 16))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.dark_mode_var = tk.IntVar()
        self.dark_mode_button = tk.Checkbutton(self.master, text="Dark Mode",
                                               variable=self.dark_mode_var,
                                               command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=4, column=0)

        self.new_game_button = tk.Button(self.master, text="New Game",
                                         command=self.new_game)
        self.new_game_button.grid(row=4, column=2)

    def make_move(self, i, j):
        if self.board[i][j] is not None:
            return
        self.board[i][j] = self.turn
        self.update_button_text(i, j)
        self.check_win()
        self.toggle_turn()

    def update_button_text(self, i, j):
        self.buttons[i][j].config(text=self.turn)

    def toggle_turn(self):
        self.turn = "O" if self.turn == "X" else "X"
        self.turn_label.config(text=f"Turn: {self.turn}")

    def check_win(self):
        for player in ["X", "O"]:
            for i in range(3):
                if all(self.board[i][j] == player for j in range(3)) or \
                        all(self.board[j][i] == player for j in range(3)) or \
                        all(self.board[i][i] == player for i in range(3)) or \
                        all(self.board[i][2 - i] == player for i in range(3)):
                    self.win(player)
                    return
        if all(cell is not None for row in self.board for cell in row):
            self.win(None)

    def win(self, player):
        message = "Draw!" if player is None else f"Player {player} wins!"
        messagebox.showinfo("Tic Tac Toe", message)

    def toggle_dark_mode(self):
        bg = "black" if self.dark_mode_var.get() else "white"
        fg = "white" if self.dark_mode_var.get() else "black"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(bg=bg, fg=fg)
        self.turn_label.config(bg=bg, fg=fg)
        self.dark_mode_button.config(bg=bg, fg=fg)
        self.new_game_button.config(bg=bg, fg=fg)

    def new_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.update_buttons_text()

    def update_buttons_text(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
