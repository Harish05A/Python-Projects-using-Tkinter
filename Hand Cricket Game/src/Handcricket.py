import tkinter as tk
from tkinter import messagebox
import random

class HandCricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Cricket Game")
        self.root.geometry("400x300")
        
        self.user_score = 0
        self.computer_score = 0
        self.is_user_batting = True
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose a number between 1 and 6")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Your Score: 0 | Computer Score: 0")
        self.score_label.pack(pady=10)
    
    def play(self):
        user_choice = int(self.entry.get())
        if user_choice < 1 or user_choice > 6:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 6")
            return
        
        computer_choice = random.randint(1, 6)
        
        if user_choice == computer_choice:
            if self.is_user_batting:
                self.result_label.config(text=f"Out! You scored {self.user_score} runs.")
                self.is_user_batting = False
                self.user_score = 0
            else:
                self.result_label.config(text=f"Computer is out! Computer scored {self.computer_score} runs.")
                self.check_winner()
                self.reset_game()
        else:
            if self.is_user_batting:
                self.user_score += user_choice
                self.result_label.config(text=f"You scored {user_choice} runs.")
            else:
                self.computer_score += computer_choice
                self.result_label.config(text=f"Computer scored {computer_choice} runs.")
        
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")
    
    def check_winner(self):
        if self.user_score > self.computer_score:
            messagebox.showinfo("Game Over", "You win!")
        elif self.user_score < self.computer_score:
            messagebox.showinfo("Game Over", "Computer wins!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.is_user_batting = True
        self.result_label.config(text="")
        self.score_label.config(text="Your Score: 0 | Computer Score: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = HandCricketGame(root)
    root.mainloop()
