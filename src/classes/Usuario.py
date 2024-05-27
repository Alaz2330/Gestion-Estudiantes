from src.util.db import *
class Usuario:
    def __init__(self, userName: str, id: str, password: str, nombre: str, edad: str, genero: str, direccion: str, cellphone: str, email: str):
        self.userName = userName
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad 
        self.genero = genero 
        self.direccion = direccion
        self.cellphone = cellphone
        self.email = email

    def crearUsuario(self):
        try:
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
            con.close()
            print("Se creo el usuario con exito")
        except Exception as e:
            print("Ups, ah ocurrido un error")
            print(e)
    
    def leerInformacionUsuario(self):
        try:
            con,cur = connectDatabase()
            rowData = cur.execute(f''' select * from users where id='{self.id}';''')
            user = None
            for user in rowData:
                user = Usuario(user["userName"],user["id"],
                    user["password"],user["nombre"],
                    user["edad"],user["genero"],user["direccion"],
                    user["cellphone"],user["email"])
            con.commit()
            con.close()
            return rowData
        except:
            print("Ups, ah ocurrido un error")
            return None
    
    def actualizarUsuario(self,atributo,valor):
        try:
            con,cur = connectDatabase()
            cur.execute(f'''UPDATE Users
                        SET {atributo}='{valor}'
                        WHERE id='{self.id}';
                        ''')
            con.commit()
            con.close()
            return "Se actualizo con exito"
        except:
            return "Ups, ah ocurrido un error"
    def mostrarUsuario(self):
        print(self.userName, self.id, self.password, self.nombre, self.edad, self.genero, self.direccion, self.cellphone, self.email)

def checkUsuario(userName, password):
    try:
        con,cur = connectDatabase()
        rowData = cur.execute(f''' select * from Users where userName='{userName}' AND password='{password}';''')
        user = None
        for data in rowData:
            tipo = data["tipo"]
            user = Usuario(data["userName"], data["id"], data["password"],data["nombre"],data["edad"]
                ,data["genero"],data["direccion"],data["cellphone"], data["email"])      
        con.commit()
        con.close()
        return tipo, user
    except Exception as e:
        print("Ups, ha ocurrido un error")
        print(e)
        return None, None

def actualizarUsuario(id,atributo,valor):
    try:
        con,cur = connectDatabase()
        cur.execute(f'''UPDATE Users
                    SET {atributo}='{valor}'
                    WHERE id='{id}';
                    ''')
        con.commit()
        con.close()
        return "Se actualizo con exito"
    except:
        return "Ups, ah ocurrido un error"