from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        root.title("PyScott")
        root.geometry("200x400")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid()

        ttk.Button(self.frame, text="Empleados", command=root.destroy).grid(column=0, row=0)

        ttk.Button(self.frame, text="Departamentos", command=root.destroy).grid(column=0, row=1)

