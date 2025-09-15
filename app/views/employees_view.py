import tkinter as tk
from tkinter import ttk, messagebox
from app.models.employee import Employee

class EmployeesView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados (Oracle + Python)")
        self.root.geometry("700x500")

        # --- Formulario de entrada ---
        form_frame = ttk.LabelFrame(root, text="Formulario Empleado", padding=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(form_frame, text="EMPNO:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.empno_entry = ttk.Entry(form_frame)
        self.empno_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="ENAME:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.ename_entry = ttk.Entry(form_frame)
        self.ename_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="JOB:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.job_entry = ttk.Entry(form_frame)
        self.job_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="DEPTNO:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.deptno_entry = ttk.Entry(form_frame)
        self.deptno_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botones CRUD
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Crear", command=self.create_employee).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.get_employee).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_employee).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.delete_employee).pack(side="left", padx=5)

        # --- Tabla de resultados ---
        table_frame = ttk.LabelFrame(root, text="Empleados", padding=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("empno", "ename", "job", "deptno"), show="headings")
        self.tree.heading("empno", text="EMPNO")
        self.tree.heading("ename", text="ENAME")
        self.tree.heading("job", text="JOB")
        self.tree.heading("deptno", text="DEPTNO")
        self.tree.pack(fill="both", expand=True)

    def create_employee(self):
        try:
            empno = int(self.empno_entry.get())
            ename = self.ename_entry.get()
            job = self.job_entry.get()
            deptno = int(self.deptno_entry.get())
            Employee.create(empno, ename, job, deptno)
            messagebox.showinfo("Éxito", "Empleado creado correctamente")
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear: {e}")

    def get_employee(self):
        try:
            empno = int(self.empno_entry.get())
            emp = Employee.get(empno)
            if emp:
                self.ename_entry.delete(0, tk.END)
                self.ename_entry.insert(0, emp[1])
                self.job_entry.delete(0, tk.END)
                self.job_entry.insert(0, emp[2])
                self.deptno_entry.delete(0, tk.END)
                self.deptno_entry.insert(0, emp[3])
                messagebox.showinfo("Encontrado", f"Empleado {emp[1]} encontrado")
            else:
                messagebox.showwarning("No encontrado", "Empleado no existe")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar: {e}")

    def update_employee(self):
        try:
            empno = int(self.empno_entry.get())
            job = self.job_entry.get()
            Employee.update(empno, job)
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {e}")

    def delete_employee(self):
        try:
            empno = int(self.empno_entry.get())
            Employee.delete(empno)
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {e}")

    def refresh_table(self):
        """Recarga la tabla con los empleados actuales"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Esto es solo un ejemplo, deberías crear un método get_all en Employee
        # Aquí muestro solo uno si buscas
        empno = self.empno_entry.get()
        if empno:
            emp = Employee.get(int(empno))
            if emp:
                self.tree.insert("", "end", values=emp)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeesView(root)
    root.mainloop()