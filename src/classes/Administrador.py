from src.classes.Usuario import Usuario
from src.util.db import connectDatabase

class Administrador(Usuario):
    def consultarEstudiante(busqueda):
        try:
            con,cur = connectDatabase()
            rowData = cur.execute(f''' select * from users where id like '%{busqueda}%' or name like '%{busqueda}%';''')
            users = ()
            for data in rowData:
                user = Usuario(data["userName"],data["id"],
                    data["password"],data["nombre"],
                    data["edad"],data["genero"],data["direccion"],
                    data["cellphone"],data["email"])
                users.append(user)
            con.commit()
            con.close()           
            return users
        except:
            print("Ups, ah ocurrido un error")
            return None