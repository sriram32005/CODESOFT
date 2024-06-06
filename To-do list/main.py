import tkinter as tk

class TodoApp:
    def __init__(self,root):
        self.root = root
        root.title("To-Do List")

        self.tasks = []

        self.label1 = tk.Label(root,text="Welcome to your to-do list")
        self.label1.pack(side=tk.TOP)

        self.label2 = tk.Label(root,text="Enter new task here: ")
        self.label2.pack(pady=(10,0))

        self.inp_box = tk.Entry(root,width=40)
        self.inp_box.pack(pady=10)

        self.add_btn = tk.Button(root,text="Add Task",command=self.add)
        self.add_btn.pack(pady=(0,10))

        self.label3 = tk.Label(root,text="Your Tasks")
        self.label3.pack(pady=(10,0))

        self.task_box = tk.Listbox(width=60)
        self.task_box.pack(padx=20)

        self.label4 = tk.Label(root,text="Please select a task to Remove or Mark as Done.")
        self.label4.pack(pady=(10,0))

        self.rm_btn = tk.Button(root,text="Remove Task",command=self.remove)
        self.rm_btn.pack(side=tk.LEFT,padx=(30,15),pady=20)

        self.mad_btn = tk.Button(root,text="Mark as Done",command=self.mark_as_done)
        self.mad_btn.pack(side=tk.RIGHT,padx=(15,30),pady=(10,20))

    def add(self):
        cur_tsk = self.inp_box.get()
        print(cur_tsk)
        if cur_tsk:
            self.tasks.append([cur_tsk,False])
            self.task_box.insert(tk.END,cur_tsk)
            self.inp_box.delete(0,tk.END)
        else:
            print("Not working")

    def remove(self):
        cur_tsk = self.task_box.curselection()
        if cur_tsk:
            print(cur_tsk)
            index=cur_tsk[0]
            del self.tasks[index]
            self.task_box.delete(index)

    def mark_as_done(self):
        cur_tsk = self.task_box.curselection()
        if cur_tsk:
            index = cur_tsk[0]
            self.tasks[index][1] = True
            if not self.tasks[index][0].endswith("  (Done)"):
                self.tasks[index][0] += "  (Done)" 
            self.task_box.delete(index)
            self.task_box.insert(index,self.tasks[index][0])
            self.task_box.itemconfig(index,{"bg":"light blue"})

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()