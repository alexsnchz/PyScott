from tkinter import Tk
from app.views.main_window import MainWindow

def main():
    """
    Clase principal del aplicativo que carga la vista principal encargada
    de crear el layout principal.
    """
    root = Tk()

    """ Referencia a la vista de ventana principal """
    MainWindow(root)
    
    """ Corre Tkiter del objeto instanciado """
    root.mainloop()

if __name__ == "__main__":
    main()