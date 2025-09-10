# PyScott
Proyecto de aplicación CRUD Python usando schema Scott

## Especificaciones
Desarrollar una aplicación en Python que permita realizar operaciones CRUD
(Create, Read, Update, and Delete) sobre el esquema de Scott de Oracle
mediante el drive oracledb


## Base de datos
- Oracle 21.3.0 XE
- [Schema Scott](https://github.com/oracle/dotnet-db-samples/blob/master/schemas/scott.sql)

## Aplicativo
- Python 3.12.10

## Ejecución
#### Docker OracleDB
```bash
cd ./oracle/
docker-compose up -d
```

## Estructura de proyecto
```bash
PyScott
├───.env
├───.env.example
├───.gitignore
├───README.md
│
├───.venv
│
├───app
│       main.py
│
└───oracle
    │   docker-compose.yml
    │
    └───scripts
        └───setup
                scott.sql
```
