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

### Aplicación
```bash
python -m app.main
```

## Estructura de proyecto
```bash
PyScott
├───.env
├───.env.example
├───.gitignore
├───README.md
├───.venv/
├───app
│   ├───.env
│   ├───.env.example
│   ├───main.py
│   ├───requirements.txt
│   ├───__init__.py
│   ├───config
│   │   ├───db.py
│   │   └───__init__.py
│   ├───views
│   │   ├───departments_view.py
│   │   ├───employees_view.py
│   │   ├───main_window.py
│   │   └───__init__.py
│   └───models
│       ├───department.py
│       ├───employee.py
│       └───__init__.py
└───oracle
    ├───.env
    ├───.env.example
    ├───docker-compose.yml
    └───scripts
        ├───setup
        │   └───scott.sql 
        ├───startup
        └───queries.sql
```
