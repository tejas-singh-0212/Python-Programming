import tkinter as tk
from tkinter import ttk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.status_label = None
        self.create_board()
        self.reset_button = ttk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
        if self.status_label:
            self.status_label.destroy()
            self.status_label = None

    def create_board(self):
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
            for j in range(3):
                btn = ttk.Button(self.root, text="", command=lambda r=i, c=j: self.make_move(r, c))
                btn.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                self.buttons[i][j] = btn

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["state"] = "disabled"
            
            if self.check_winner():
                self.display_winner()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                self.display_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def display_winner(self):
        self.status_label = ttk.Label(self.root, text=f"Player {self.current_player} wins!")
        self.status_label.grid(row=3, column=0, columnspan=3)
        self.disable_all_buttons()

    def display_draw(self):
        self.status_label = ttk.Label(self.root, text="It's a draw!")
        self.status_label.grid(row=3, column=0, columnspan=3)
        self.disable_all_buttons()

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = "disabled"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()