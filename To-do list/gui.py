import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-do list")
        label=tk.Label(self,text="Welcome to your To-do list!")
        label.pack(fill=tk.BOTH,expand=1,padx=100,pady=30)

        e_button = tk.Button(self,text="Enter",command=self.add)
        e_button.pack(padx=20,pady=30,side=tk.BOTTOM)

    def add(self):
        textin=input()
        new=tk.Label(self,text=textin+"\n")
        new.pack(side=tk.LEFT,fill=tk.BOTH,expand=1,padx=(10,10),pady=10)



if __name__=="__main__":
    window=Window()
    window.mainloop()