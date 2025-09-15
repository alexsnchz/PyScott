from config.db import open_connection

class Department:
    @staticmethod
    def create(empno, ename, job, deptno):
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO EMP (EMPNO, ENAME, JOB, DEPTNO)
                VALUES (:1, :2, :3, :4)
                """,
                [empno, ename, job, deptno]
            )
        conn.commit()

    @staticmethod
    def get(empno):
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT EMPNO, ENAME, JOB, DEPTNO FROM EMP WHERE EMPNO=:1", [empno])
            return cursor.fetchone()

    @staticmethod
    def update(empno, job):
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE EMP SET JOB=:1 WHERE EMPNO=:2", [job, empno])
        conn.commit()

    @staticmethod
    def delete(empno):
        conn = open_connectionn()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM EMP WHERE EMPNO=:1", [empno])
        conn.commit()