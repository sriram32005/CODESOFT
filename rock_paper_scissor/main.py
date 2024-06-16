import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        root.title("Rock Paper Scissors")

        self.user_choice = tk.StringVar()
        self.comp_choice = tk.StringVar()

        self.label = tk.Label(root, text="Let's play:: Choose one:")
        self.label.pack()

        self.rock = tk.Button(root, text="Rock", command=lambda: self.play("Rock"))
        self.rock.pack(padx=80,pady=10)

        self.paper = tk.Button(root, text="Paper", command=lambda: self.play("Paper"))
        self.paper.pack(padx=80,pady=10)

        self.scissors = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors.pack(padx=80,pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.comp_score = tk.IntVar()
        self.user_score = tk.IntVar()

        self.score_track = tk.Label(root,text = f"User Score: {self.user_score.get()} :: Computer Score: {self.comp_score.get()}")
        self.score_track.pack()

    def play(self, user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.user_choice.set(f"Your choice: {user_choice}")
        self.comp_choice.set(f"Computer's choice: {comp_choice}")

        if user_choice == comp_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You win!"
            self.user_score.set(self.user_score.get()+1)
            self.score_track.configure(text=f"User Score: {self.user_score.get()} :: Computer Score: {self.comp_score.get()}")
        else:
            result = "Computer wins!"
            self.comp_score.set(self.comp_score.get()+1)
            self.score_track.configure(text=f"User Score: {self.user_score.get()} :: Computer Score: {self.comp_score.get()}")

        self.result_label.config(text=result)
        proceed = messagebox.askyesno("Proceed?",f"{self.comp_choice.get()}\n {self.user_choice.get()}\n \"{result}\",  Wanna play another round?")
        if not proceed:
            if self.comp_score.get() > self.user_score.get():
                msg = "Computer Wins!!"
            elif self.comp_score.get() < self.user_score.get():
                msg = "You Win!!"
            else:
                msg = "It's a tie."
            messagebox.showinfo("Result",msg)
            root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
