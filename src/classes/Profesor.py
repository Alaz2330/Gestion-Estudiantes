from src.classes.Usuario import Usuario
from src.classes.Asignatura import Asignatura
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

def consultarAsignatura(self): 
    try:
       con,cur = connectDatabase()
       rowData = cur.execute(f''' select * from asignaturas where profesorId = '{self.id}';''')
       asignaturas = list()
       for data in rowData:
           asignatura = Asignatura(data["nombre"], data["profesorId"])
           asignaturas.append(asignatura)
       con.commit()
       con.close()
       return asignaturas
    except Exception as e:
        print("Ups, ha ocurrido un error")
        print(e)
        return None

def consultarEstudiante(self,identificador):
        try:
            con,cur = connectDatabase()
            rowData = cur.execute(f''' select * from users where tipo = 'estudiante' AND id like '%{identificador}%' or nombre like '%{identificador}%';''')
            users = list()
            for data in rowData:
                user = Usuario(data["userName"],data["id"],
                    data["password"],data["nombre"],
                    data["edad"],data["genero"],data["direccion"],
                    data["cellphone"],data["email"])
                users.append(user)
            con.commit()
            con.close()           
            return users
        except Exception as e:
            print("Ups, ha ocurrido un error")
            print(e)
            return None