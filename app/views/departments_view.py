import tkinter as tk
from tkinter import ttk, messagebox
from app.models.department import Department

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
        
        """ Frame formulario de búsqueda """
        search_frame = ttk.LabelFrame(self, text="Buscar empleado", padding=10)
        search_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(search_frame, text="No. departamento:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.dpto_search = ttk.Entry(search_frame)
        self.dpto_search.grid(row=0, column=1, padx=5, pady=5)

        self.search_btn = ttk.Button(search_frame, text="Buscar", command=self.get_department)
        self.search_btn.grid(row=0, column=2, padx=5, pady=5)

        """ Frame formulario de departamento """
        form_frame = ttk.LabelFrame(self, text="Formulario Departamento", padding=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(form_frame, text="No. Departamento:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.deptno_input = ttk.Entry(form_frame)
        self.deptno_input.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Departamento:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.name_input = ttk.Entry(form_frame)
        self.name_input.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Ubicación:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.loc_input = ttk.Entry(form_frame)
        self.loc_input.grid(row=2, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        """ Botones formulario de departmento """
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Crear", command=self.create_department).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_department).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.delete_department).pack(side="left", padx=5)

        """ Frame tabla de departamentos """
        table_frame = ttk.LabelFrame(self, text="Departamentos", padding=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        """ Creación de tabla de departamentos con encabezados """
        self.tree = ttk.Treeview(table_frame, columns=("deptno", "dname", "loc"), show="headings")
        self.tree.heading("deptno", text="No. Departamento:")
        self.tree.heading("dname", text="Departamento")
        self.tree.heading("loc", text="Ubicación")
        self.tree.pack(fill="both", expand=True)

        """ Llena el listado de empleados """
        self.refresh_table()


    def create_department(self):
        """
        Crea un empleado con los datos del formulario de empleados
        """

        try:
            deptno = int(self.deptno_input.get())
            dname = self.name_input.get().upper()
            loc = self.loc_input.get().upper()
            Department.create(deptno, dname, loc)
            messagebox.showinfo("Éxito", "Departamento creado correctamente.")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el departamento: {e}")


    def get_department(self):
        """
        Obtiene los datos de un empleado en base a su número de empleado
        """

        try:
            deptno = int(self.dpto_search.get())
            depto = Department.get(deptno)
            if depto:
                self.clear_form()
                self.deptno_input.insert(0, depto[0])
                self.name_input.insert(0, depto[1])
                self.loc_input.insert(0, depto[2])
            else:
                messagebox.showwarning("No encontrado", "El departamento no existe, verifica el número de departamento.")
        except Exception as e:
            messagebox.showerror("Error", f"Introduce un número de departamento válido. {e}")


    def update_department(self):
        """
        Actualiza los datos de un empleado considerando los datos del formuario
        """

        try:
            deptno = int(self.deptno_input.get())
            dname = self.name_input.get().upper()
            loc = self.loc_input.get().upper()
            Department.update(deptno, dname, loc)
            messagebox.showinfo("Éxito", "Departamento actualizado correctamente")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {e}")


    def delete_department(self):
        """
        Elimina el departamento buscado
        """

        try:
            deptno = int(self.deptno_input.get())
            Department.delete(deptno)
            messagebox.showinfo("Éxito", "Departamento eliminado correctamente")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {e}")


    def refresh_table(self):
        """
        Refresca la tabla con los datos de los departamentos
        """

        for row in self.tree.get_children():
            self.tree.delete(row)

        departments = Department.get_all()
        for depto in departments:
            self.tree.insert("", "end", values=depto)

    def clear_form(self):
        self.deptno_input.delete(0, tk.END)
        self.name_input.delete(0, tk.END)
        self.loc_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DepartmentsView(root)
    root.mainloop()