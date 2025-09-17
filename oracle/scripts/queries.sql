/*
 Inserción de un nuevo empleado dentro de la tabla employees utilizando los datos
 principales del empleado y empleando el current_timestamp como fecha de registro y
 fecha de HIREDATE.
*/
INSERT INTO
    EMP (EMPNO, ENAME, JOB, SAL, DEPTNO, MGR, HIREDATE)
VALUES
    (1, 'ALEJANDRO SÁNCHEZ', 'DEV', 200, 20, 7521, CURRENT_TIMESTAMP)


/*
 Consulta para obtener los datos principales de un empleado a consultar
 buscando por medio de su identificador unico EMPNO.
*/
SELECT
    EMPNO,
    ENAME,
    JOB,
    DEPTNO,
    SAL,
    MGR
FROM
    EMP
WHERE
    EMPNO = 1


/*
 Consulta para obtener los datos principales a desplegar de los empleados
 usando inner joins para obtener el nombre del departamento al que pertenece
 así como un left join para obtener el nombre de su gerente en caso de que aplique.
*/
SELECT
    EMP.EMPNO,
    EMP.ENAME,
    EMP.JOB,
    EMP.SAL,
    EMP.HIREDATE,
    DEPT.DNAME,
    MNGR.ENAME as MNGR
FROM
    EMP
    INNER JOIN DEPT ON DEPT.DEPTNO = EMP.DEPTNO
    LEFT JOIN EMP MNGR ON EMP.MGR = MNGR.EMPNO
ORDER BY
    EMP.EMPNO


/*
 Consulta para obtener solo el identificador del empleado y su nombre, la cual
 es utilizada para poblar dinamicamente la información del combo box de asignación
 de gerente. 
*/
select 
    EMPNO, 
    ENAME 
FROM 
    EMP 
ORDER BY 
    EMP.EMPNO


/*
 Actualización de datos del empleado seleccionado por medio de su identificador.
*/
UPDATE EMP 
SET 
    ENAME  = 'ALEX SANCHEZ M.', 
    JOB    = 'DEV', 
    SAL    = 500, 
    DEPTNO = 10, 
    MGR    = 7566
WHERE 
    EMPNO  = 1


/*
 Eliminación del registro de la tabla de empleados por seleccionando con su identificador.
*/
DELETE FROM EMP 
WHERE 
    EMPNO = 1


/*
 Inserta un nuevo registro dentro de la tabla de departamentos
*/
INSERT INTO DEPT (DEPTNO, DNAME, LOC)
    VALUES (50, 'DEVOPS', 'CHIHUAHUA')


/*
 Consulta para obtener los registros principales de un departamento seleccionado con
 su identificador único DEPTNO.
*/
SELECT 
    DEPTNO, 
    DNAME, 
    LOC 
FROM DEPT 
WHERE 
    DEPTNO = :1


/*
 Actualización de un registro seleccionando por su identificador único.
*/
UPDATE DEPT 
SET 
    DNAME  = :1, 
    LOC    = :2 
WHERE 
    DEPTNO = :3


/*
 Eliminación de un departamento seleccionado por su identificador único.
*/
DELETE FROM DEPT 
WHERE 
    DEPTNO = :1


/*
 Selección de los campos DEPTNO, DNAME y LOC de todos los registros presentes
 en la base de datos de departamentos DEPT
*/
SELECT 
    DEPTNO, 
    DNAME, 
    LOC 
FROM 
    DEPT 
ORDER BY 
    DEPTNO
