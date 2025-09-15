from tkinter import ttk, messagebox

class DepartmentsView(ttk.Frame):
    """ 
    Ventana de gestion de departamentos
    
    Carga la vista principal de departamentos que contiene un buscador,
    formulario para la creación, actualización y eliminación de departamentos
    Además de un listado con todos los departamentos presentes en base de datos.

    params:
        ttk.Frame

    """

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        """ Título """
        title_label = ttk.Label(self, text="Gestión de Departamentos", font=("Arial", 15))
        title_label.pack(pady=10)

        # --- Form ---
        form_frame = ttk.LabelFrame(self, text="Formulario Departamento", padding=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(form_frame, text="No. Departamento:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.deptno_entry = ttk.Entry(form_frame)
        self.deptno_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Departamento:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.dname_entry = ttk.Entry(form_frame)
        self.dname_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Ubicación:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.loc_entry = ttk.Entry(form_frame)
        self.loc_entry.grid(row=2, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # ttk.Button(button_frame, text="Crear", command=self.create_department).pack(side="left", padx=5)
        # ttk.Button(button_frame, text="Buscar", command=self.get_department).pack(side="left", padx=5)
        # ttk.Button(button_frame, text="Actualizar", command=self.update_department).pack(side="left", padx=5)
        # ttk.Button(button_frame, text="Eliminar", command=self.delete_department).pack(side="left", padx=5)

        # --- Tabla de resultados ---
        table_frame = ttk.LabelFrame(self, text="Departamentos", padding=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("deptno", "dname", "loc"), show="headings")
        self.tree.heading("deptno", text="No. Departamento:")
        self.tree.heading("dname", text="Departamento")
        self.tree.heading("loc", text="Ubicación")
        self.tree.pack(fill="both", expand=True)


