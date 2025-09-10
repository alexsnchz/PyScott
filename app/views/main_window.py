from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        root.title("PyScott Test")
        root.geometry("800x600")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid()

        ttk.Label(self.frame, text="Hello World!").grid(column=0, row=0)
        ttk.Button(self.frame, text="Quit", command=root.destroy).grid(column=1, row=0)

