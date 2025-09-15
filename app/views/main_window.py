from tkinter import ttk
from app.views.employees_view import EmployeesView
from app.views.departments_view import DepartmentsView

class MainWindow:
    """
    Ventana principal que contiene la vista de selección de form (Empleados o Departamentos)
    """

    def __init__(self, root):
        self.root = root
        self.root.title("PyScott")
        self.root.geometry("1200x800")

        # --- Frame lateral de menú ---
        menu_frame = ttk.Frame(self.root, padding=10)
        menu_frame.pack(side="left", fill="y")

        # --- Área central para cargar las vistas ---
        self.content_frame = ttk.Frame(self.root, padding=10)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # --- Botones de menú ---
        ttk.Button(menu_frame, text="Empleados", command=self.show_employees).pack(fill="x", pady=5)
        ttk.Button(menu_frame, text="Departamentos", command=self.show_departments).pack(fill="x", pady=5)

    def clear_content(self):
        """
        Destruye el contenido del frame de contenidos para cargar contenido nuevo
        """
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    def show_employees(self):
        """
        Carga la vista de empleados importando los datos de views/employees
        """
        self.clear_content()
        EmployeesView(self.content_frame)


    def show_departments(self):
        """
        Carga la vista de departamentos importando los datos de views/departments
        """
        self.clear_content()
        DepartmentsView(self.content_frame)
