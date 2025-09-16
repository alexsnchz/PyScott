import tkinter as tk
from tkinter import ttk, messagebox
from app.models.employee import Employee
from app.models.department import Department

class EmployeesView(ttk.Frame):
    """ 
    Ventana de gestion de empleados
    
    Carga la vista principale de empleados que contiene un buscador,
    formulario para la creación, actualización y eliminación de empleados
    Además de un listado con todos los empleados presentes en base de datos.

    params:
        ttk.Frame

    """

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        """ Título env vista """
        title_label = ttk.Label(self, text="Control de empleados", font=("Arial", 15))
        title_label.pack(pady=10)

        """ Frame formulario de búsqueda """
        search_frame = ttk.LabelFrame(self, text="Buscar empleado", padding=10)
        search_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(search_frame, text="No. empleado:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.empno_search = ttk.Entry(search_frame)
        self.empno_search.grid(row=0, column=1, padx=5, pady=5)

        self.search_btn = ttk.Button(search_frame, text="Buscar", command=self.get_employee)
        self.search_btn.grid(row=0, column=2, padx=5, pady=5)

        """ Frame formulario de empleado """
        form_frame = ttk.LabelFrame(self, text="Formulario Empleado", padding=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(form_frame, text="No. empleado:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.empno_input = ttk.Entry(form_frame, width=23)
        self.empno_input.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.name_input = ttk.Entry(form_frame, width=23)
        self.name_input.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Puesto:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.job_input = ttk.Entry(form_frame, width=23)
        self.job_input.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Salario:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.sal_input = ttk.Entry(form_frame, width=23)
        self.sal_input.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Departamento:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.depto_var = tk.StringVar()
        self.depto_select = ttk.Combobox(form_frame, textvariable=self.depto_var, state="readonly")
        self.depto_select.grid(row=4, column=1, padx=5, pady=5)

        """ Carga de datos para combo box departamentos """
        departments = Department.get_all("DEPTNO, DNAME")
        self.dept_map = {dname: deptno for deptno, dname in departments}
        self.depto_select['values'] = list(self.dept_map.keys())

        ttk.Label(form_frame, text="Gerente:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.mgr_var = tk.StringVar()
        self.mgr_select = ttk.Combobox(form_frame, textvariable=self.mgr_var, state="readonly")
        self.mgr_select.grid(row=5, column=1, padx=5, pady=5)

        """ Carga de datos para combo box gerentes """
        managers = Employee.get_all_names()
        self.mgr_map = {ename: empno for empno, ename in managers}
        self.mgr_select['values'] = list(self.mgr_map.keys())

        """ Botones formulario de empleado """
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Crear", command=self.create_employee).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_employee).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.delete_employee).pack(side="left", padx=5)

        """ Frame tabla de empleados """
        table_frame = ttk.LabelFrame(self, text="Empleados", padding=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        """ Creación de tabla de emplados con encabezados """
        self.tree = ttk.Treeview(table_frame, columns=("empno", "ename", "job", "sal", "hiredate", "depto", "mngr"), show="headings")
        self.tree.heading("empno", text="No. Emp.")
        self.tree.heading("ename", text="Nombre")
        self.tree.heading("job", text="Puesto")
        self.tree.heading("sal", text="Salario")
        self.tree.heading("hiredate", text="Contratación")
        self.tree.heading("depto", text="Departamento")
        self.tree.heading("mngr", text="Gerente")
        self.tree.pack(fill="both", expand=True)

        """ Llena el listado de empleados """
        self.refresh_table()


    def create_employee(self):
        """
        Crea un empleado con los datos del formulario de empleados
        """

        try:
            empno = int(self.empno_input.get())
            ename = self.name_input.get().upper()
            job = self.job_input.get().upper()
            deptno = self.dept_map[self.depto_var.get()]
            sal = int(self.sal_input.get())
            mgr = self.mgr_map.get(self.mgr_var.get())
            Employee.create(empno, ename, job, sal, deptno, mgr)
            messagebox.showinfo("Éxito", "Empleado creado correctamente")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear: {e}")


    def get_employee(self):
        """
        Obtiene los datos de un empleado en base a su número de empleado
        """

        try:
            empno = int(self.empno_search.get())
            emp = Employee.get(empno)
            if emp:
                self.clear_form()
                self.empno_input.insert(0, emp[0])
                self.name_input.insert(0, emp[1])
                self.job_input.insert(0, emp[2])
                self.depto_select.insert(0, emp[3])
                self.sal_input.insert(0, emp[4])
                self.mgr_select.insert(0, emp[5])
            else:
                messagebox.showwarning("No encontrado", "El empleado no existe, verifica el número de empleado.")
        except Exception as e:
            messagebox.showerror("Error", f"Introduce un número de empleado válido.")


    def update_employee(self):
        """
        Actualiza los datos de un empleado considerando los datos del formuario
        """

        try:
            empno = int(self.empno_input.get())
            job = self.job_input.get().upper()
            Employee.update(empno, job)
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {e}")


    def delete_employee(self):
        """
        Elimina un empleado búscado
        """

        try:
            empno = int(self.empno_input.get())
            Employee.delete(empno)
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
            self.clear_form()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {e}")


    def refresh_table(self):
        """
        Refresca la tabla con los datos de empleados
        """

        for row in self.tree.get_children():
            self.tree.delete(row)

        employees = Employee.get_all()
        for emp in employees:
            self.tree.insert("", "end", values=emp)

    def clear_form(self):
        self.empno_input.delete(0, tk.END)
        self.name_input.delete(0, tk.END)
        self.job_input.delete(0, tk.END)
        self.depto_select.delete(0, tk.END)
        self.sal_input.delete(0, tk.END)
        self.mgr_select.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeesView(root)
    root.mainloop()