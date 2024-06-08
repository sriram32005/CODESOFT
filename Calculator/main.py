import tkinter as tk
from tkinter import messagebox

class Calulator:
    def __init__(self,root):
        self.root = root
        root.title("Calc")
        root.configure(bg="grey")

        self.n1_box = tk.Entry(root)
        self.n1_box.pack(pady=20,padx=40)
        self.n2_box = tk.Entry(root)
        self.n2_box.pack(pady=20,padx=40)

        self.operation = tk.StringVar()
        self.operation.set("Select operation")

        self.menu = tk.OptionMenu(root,self.operation,"Add","Subtract","Multiply","Divide")
        self.menu.pack(pady=10)

        self.button = tk.Button(root,text="calculate",command=self.calulate)
        self.button.pack(pady=20)

        self.ans = tk.Label(root,text="",background="grey")
        self.ans.pack(pady=(0,20))

    def calulate(self):
        num1 = float(self.n1_box.get())
        num2 = float(self.n2_box.get())
        op = self.operation.get()

        if op == "Select operation":
            messagebox.showwarning("Warning","Select an operation to perform")
            result = "--"
        elif op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1*num2
        elif op == "Divide":
            if num2 == 0:
                messagebox.showerror("Error","Can't divide by 0")
                result = "--"
            else:
                result = num1/num2
        else:
            messagebox.showerror("Error","Unexpected error")
            result = "--"

        self.ans.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    calcapp = Calulator(root)
    root.mainloop()
