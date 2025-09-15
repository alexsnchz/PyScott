from tkinter import *
from app.views.main_window import MainWindow

def main():
    root = Tk()

    # Referencia a la vista de ventana principal
    app = MainWindow(root)
    
    # Corre Tkiter del objeto instanciado
    root.mainloop()

if __name__ == "__main__":
    main()