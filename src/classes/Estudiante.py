from src.classes.Usuario import Usuario
from src.util.db import connectDatabase

class Estudiante(Usuario):
    def __init__(self, userName, id, password, nombre, edad, genero, direccion, cnumber, email, asignatura):
        super().__init__(user, id, psd, nombre, edad, genero, direccion, cnumber, email)
        self.agregarAsignatura(asignatura)

    def agregarAsignatura(self,valor):
        self._asignatura = valor

    def crearUsuario(self):
        try:
            con,cur = connectDatabase()
            tipo = "estudiante"
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
        except:
            print("Ups, ah ocurrido un error")
