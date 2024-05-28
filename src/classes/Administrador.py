from src.classes.Usuario import Usuario
from src.util.db import connectDatabase

class Administrador(Usuario):
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
            print("Ups, ah ocurrido un error")
            print(e)
            return None
        
    def consultarProfesores(self):
        try:
            con,cur = connectDatabase()
            rowData = cur.execute(f''' select * from users where tipo = 'profesor';''')
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
            print("Ups, ah ocurrido un error")
            print(e)
            return None
    
    def crearAsignatura(self, nombre, profesorId):
        try:
            con,cur = connectDatabase()
            cur.execute(f''' 
                INSERT INTO Asignaturas
                (nombre, profesorId)
                VALUES('{nombre}', '{profesorId}');
            ''')
            con.commit()
            con.close()
            print("Se creo la asignatura con exito.")
        except Exception as e:
            print("Ups, ah ocurrido un error.")
            print(e)