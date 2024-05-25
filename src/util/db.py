import sqlite3

def connectDatabase():
    con = sqlite3.connect()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con,cur

def dbSeeder():
    con, cur = connectDatabase()
    cur.execute("PRAGMA foreign_keys = ON;")
    con.commit()
    cur.execute(
                '''CREATE TABLE IF NOT EXISTS users (
                    id TEXT NOT NULL,
                    password TEXT NOT NULL,
                    userName TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    edad TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    cellphone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    CONSTRAINT Users_PK PRIMARY KEY (id)
                ;)
                ''')
    con.commit()
    cur.execute(
                '''CREATE TABLE IF NOT EXISTS Asginaturas (
                nombre TEXT NOT NULL,
                profesorId TEXT NOT NULL,
                CONSTRAINT NewTable_PK PRIMARY KEY (nombre),
                FOREIGN KEY (profesorId) REFERENCES Users(id)
                );
            ''')
    con.commit()
    cur.execute(
                ''' CREATE TABLE IF NOT EXISTS Notas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                asignaturaNombre TEXT NOT NULL,
                estudianteId TEXT NOT NULL,
                porcentaje REAL NOT NULL,
                FOREIGN KEY (asignaturaNombre) REFERENCES Asignaturas(nombre)
                FOREIGN KEY (estudianteId) REFERENCES Users(id)
                );
            ''')
    con.commit()
    
    try:
        cur.execute(
            ''' 
            INSERT INTO Users (id,password,userName,nombre,edad,genero,direccion,cellphone,email,tipo) VALUES
            ('123','pass','alejandro','alejandro','24','Masculino','test','3182793571','alejandro77arias@gmail.com','administrador')
            ''')
        con.commit()
    except:
        print("Seeder update")