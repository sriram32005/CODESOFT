import random
import tkinter as tk

class Password_Generator:
    def __init__(self,root):
        self.root = root
        root.title("Password Generator")
        root.configure(bg="grey")

        self.lab1 = tk.Label(root,text="Password Genrator",font=("Arial",20))
        self.lab1.pack(pady=20,padx=10)

        self.lab2 = tk.Label(root,text="Enter the length of password: ")
        self.lab2.pack()

        self.len = tk.Entry(root)
        self.len.pack(pady=(5,10))

        self.lab3 = tk.Label(root,text="choose the complexity: ")
        self.lab3.pack(pady=(5,5))

        self.var1,self.var2,self.var3,self.var4 = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()

        self.c1 = tk.Checkbutton(root,text="Numbers",onvalue=1,offvalue=0,variable=self.var1)
        self.c1.pack(pady=5,padx=10)
        self.c2 = tk.Checkbutton(root,text="Lower case alphabets",onvalue=1,offvalue=0,variable=self.var2)
        self.c2.pack(pady=5,padx=10)
        self.c3 = tk.Checkbutton(root,text="Upper case alphabets",onvalue=1,offvalue=0,variable=self.var3)
        self.c3.pack(pady=5,padx=10)
        self.c4 = tk.Checkbutton(root,text="Symbols",onvalue=1,offvalue=0,variable=self.var4)
        self.c4.pack(pady=5,padx=10)

        self.button = tk.Button(root,text="Generate!",command=self.generator)
        self.button.pack(pady=20,padx=10)

        self.ans = tk.Label(root,text="",background="grey")
        self.ans.pack(side=tk.BOTTOM,pady=20)

    def generator(self):
        base=""
        ans=""
        if self.var1.get():
            base+="1234567890"
        if self.var2.get():
            base+="abcdefghijklmnopqrstuvwxyz"
        if self.var3.get():
            base+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.var4.get():
            base+="`~!@#$%^&*()-=_+[]{}\\|'\";:.,<>?/"
        
        for i in range(int(self.len.get())):
            ans+=random.choice(base)
        
        self.ans.configure(text=f"Your password: {ans}")

if __name__ == "__main__":
    root = tk.Tk()
    pswd_gen_app = Password_Generator(root)
    root.mainloop()

