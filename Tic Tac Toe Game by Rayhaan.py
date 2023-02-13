import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe by Rayhaan")

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", font=("Helvetica", 32),
                                   width=4, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.turn_label = tk.Label(master, text=f"Turn: {self.turn}",
                                   font=("Helvetica", 16))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.dark_mode_var = tk.IntVar()
        self.dark_mode_button = tk.Checkbutton(master, text="Dark Mode",
                                               variable=self.dark_mode_var,
                                               command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=4, column=0)

        self.new_game_button = tk.Button(master, text="New Game",
                                         command=self.new_game)
        self.new_game_button.grid(row=4, column=2)

        self.toggle_dark_mode()

    def make_move(self, i, j):
        if self.board[i][j] is not None:
            return
        self.board[i][j] = self.turn
        self.buttons[i][j].config(text=self.turn)
        self.check_win()
        self.turn = "O" if self.turn == "X" else "X"
        self.turn_label.config(text=f"Turn: {self.turn}")

    def check_win(self):
        # Check rows
        for row in self.board:
            if all(cell == "X" for cell in row):
                self.win("X")
                return
            if all(cell == "O" for cell in row):
                self.win("O")
                return

        # Check columns
        for j in range(3):
            if all(self.board[i][j] == "X" for i in range(3)):
                self.win("X")
                return
            if all(self.board[i][j] == "O" for i in range(3)):
                self.win("O")
                return

        # Check diagonals
        if all(self.board[i][i] == "X" for i in range(3)):
            self.win("X")
            return
        if all(self.board[i][2-i] == "X" for i in range(3)):
            self.win("X")
            return
        if all(self.board[i][i] == "O" for i in range(3)):
            self.win("O")
            return
        if all(self.board[i][2-i] == "O" for i in range(3)):
            self.win("O")
            return

        # Check for draw
        if all(cell is not None for row in self.board for cell in row):
            self.win(None)

    def win(self, player):
        if player is None:
            message = "Draw!"
        else:
            message = f"Player {player} wins!"
        messagebox.showinfo("Tic Tac Toe", message)

    def toggle_dark_mode(self):
        bg = "black" if self.dark_mode_var.get() else "white"
        fg = "white" if self.dark_mode_var.get() else "black"
        for row in self.buttons:
            for button in row:
                button.config(bg=bg, fg=fg)
        self.turn_label.config(bg=bg, fg=fg)
        self.dark_mode_button.config(bg=bg, fg=fg)
        self.new_game_button.config(bg=bg, fg=fg)

    def new_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        for row in self.buttons:
            for button in row:
                button.config(text=" ")
        self.turn_label.config(text=f"Turn: {self.turn}")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
