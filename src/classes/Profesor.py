from src.classes.Usuario import Usuario
from src.util.db import connectDatabase

class Profesor(Usuario):
    def crearUsuario(self):
        try:
            con,cur = connectDatabase()
            tipo = "profesor"
            cur.execute(f''' 
                INSERT INTO Users
                (id, password, userName, nombre, edad, genero, direccion, cellphone, email, tipo)
                VALUES('{self.id}', '{self.password}', '{self.userName}', 
                '{self.nombre}', '{self.edad}', '{self.genero}', 
                '{self.direccion}', '{self.cellphone}', '{self.email}', '{tipo}');
            ''')
            con.commit()
            print("Se creo el usuario con exito")
        except:
            print("Ups, ah ocurrido un error")