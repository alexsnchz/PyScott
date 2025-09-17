from app.config.db import open_connection, close_connection

class Employee:
    """
    Modelo para la gestión de operaciones en BD de la tabla EMP
    """

    @staticmethod
    def create(empno, ename, job, sal, deptno, mgr):
        """
        Método estático que realiza una inserción en la tabla EMP

        params:
            empno  - Número de empleado
            ename  - Nombre del empleado
            job    - Puesto del empleado
            sal    - Salario
            deptno - Número de departamento
            mgr    - Gerente
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO EMP (EMPNO, ENAME, JOB, SAL, DEPTNO, MGR, HIREDATE)
                VALUES (:1, :2, :3, :4, :5, :6, CURRENT_TIMESTAMP)
                """,
                [empno, ename, job, sal, deptno, mgr]
            )
        conn.commit()
        close_connection()

    @staticmethod
    def get(empno):
        """
        Método estático que obtiene la información de un empleado basado 
        en su número de empleado.

        params:
            empno  - Número de empleado
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT EMPNO, ENAME, JOB, DEPTNO, SAL, MGR FROM EMP WHERE EMPNO=:1", [empno])
            return cursor.fetchone()
        
    @staticmethod
    def get_all():
        """
        Método estático que obtiene todos los valores de la tabla EMP
        junto con el nombre del departamento al que pertenece.
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT EMP.EMPNO, EMP.ENAME, EMP.JOB, EMP.SAL, EMP.HIREDATE, DEPT.DNAME, MNGR.ENAME as MNGR 
                FROM EMP INNER JOIN DEPT ON DEPT.DEPTNO = EMP.DEPTNO LEFT JOIN EMP MNGR ON EMP.MGR = MNGR.EMPNO 
                ORDER BY EMP.EMPNO
                """
            )
            return cursor.fetchall()
        
    @staticmethod
    def get_all_names():
        """
        Método estático que obtiene los campos EMPNO y ENAME de todos los 
        registros en la tabla EMP.
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("select EMPNO, ENAME FROM EMP ORDER BY EMP.EMPNO")
            return cursor.fetchall()

    @staticmethod
    def update(empno, ename, job, sal, deptno, mgr):
        """
        Método estático que realiza un update en la tabla EMP usando el
        empno como identificador del row a modificar.

        params:
            empno  - Número de empleado
            job    - Puesto del empleado
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE EMP SET ENAME=:1, JOB=:2, SAL=:3, DEPTNO=:4, MGR=:5 WHERE EMPNO=:6", 
                           [ename, job, sal, deptno, mgr, empno]
                           )
        conn.commit()
        close_connection()

    @staticmethod
    def delete(empno):
        """
        Método estático que elimina un row de la tabla EMP utilizando
        el empno como identificador del row a eliminar.

        params:
            empno  - Número de empleado
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM EMP WHERE EMPNO=:1", [empno])
        conn.commit()
        close_connection()
