from src.util.db import *
class Usuario:
    def __init__(self, user: str, id: str, password: str, nombre: str, edad: str, genero: str, direccion: str, cellphonen: str, email: str):
        self.user = user
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad 
        self.genero = genero 
        self.direccion = direccion
        self.cellphone = cellphone
        self.email = email

    def crearUsuario(self):
        con,cur = connectDatabase()
        tipo = "administrador"
        cur.execute(f''' 
        INSERT INTO Users
        (id, password, userName, nombre, edad, genero, direccion, cellphone, email, tipo)
        VALUES('{self.id}', '{self.password}', '{self.userName}', 
        '{self.nombre}', '{self.edad}', '{self.genero}', 
        '{self.direccion}', '{self.cellphone}', '{self.email}', '{tipo}');
        ''')
        con.commit()

def checkUsuario(userName, password):
    try:
        con,cur = connectDatabase()
        rowData = cur.execute(f''' select * from users where userName='{userName}' AND password='{password}';''')
        user = None
        for data in rowData:
            tipo = data["tipo"]
            user = Usuario(data["userName"], data["id"], data["password"],data["edad"]
                ,data["genero"],data["direccion"],data["cellphone"], data["email"])      
        con.commit()
        return tipo, user
    except:
        print("Ups, ha ocurrido un error")
        return None, None