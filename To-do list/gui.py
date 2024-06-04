import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-do list")

        label=tk.Label(self,text="Welcome to your To-do list!")
        label.pack(fill=tk.BOTH,expand=1,padx=100,pady=250)


if __name__=="__main__":
    window=Window()
    window.mainloop()