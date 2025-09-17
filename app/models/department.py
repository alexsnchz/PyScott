from app.config.db import open_connection, close_connection

class Department:
    """
    Modelo para la gestión de operaciones en BD de la tabla DEPT
    """

    @staticmethod
    def create(deptno, dname, loc):
        """
        Método estático que realiza una inserción en la tabla DEPT

        params:
            deptno - Número de departamento
            dname  - Nombre del departamento
            loc    - Ubicación
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO DEPT (DEPTNO, DNAME, LOC)
                VALUES (:1, :2, :3)
                """,
                [deptno, dname, loc]
            )
        conn.commit()
        close_connection()

    @staticmethod
    def get(deptno):
        """
        Función estática que obtiene un registro de tabla DEPT
        filtrando por deptno.

        params:
            deptno - Número de departamento
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT DEPTNO, DNAME, LOC FROM DEPT WHERE DEPTNO=:1", [deptno])
            return cursor.fetchone()

    @staticmethod
    def update(deptno, dname, loc):
        """
        Método estático que realiza una actualización en un row en la tabla DEPT
        basado en el deptno

        params:
            deptno - Número de departamento
            dname  - Nombre del departamento
            loc    - Ubicación
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE DEPT SET DNAME=:1, LOC=:2 WHERE DEPTNO=:3", [dname, loc, deptno])
        conn.commit()
        close_connection()

    @staticmethod
    def delete(deptno):
        """
        Método estático que elimina un row de la tabla DEPT basado en el deptno

        params:
            deptno - Número de departamento
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM DEPT WHERE DEPTNO=:1", [deptno])
        conn.commit()
        close_connection()

    @staticmethod
    def get_all(select = "DEPTNO, DNAME, LOC"):
        """
        Función estática que obtiene todos los registros de la tabla DEPT
        
        params:
            select - Campos a obtener en el resultado (opcional)
        """
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT {select} FROM DEPT ORDER BY DEPTNO")
            return cursor.fetchall()
