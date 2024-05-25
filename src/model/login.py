from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador
from src.classes.Usuario import checkUsuario

def login():   
    while True:
        userName = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        tipo, user = checkUsuario(userName,password)
        currentUser = None
        if(tipo == "administrador"):
            currentUser = Administrador(user.userName,user.id,
                user.password,user.nombre,user.edad,user.genero,
                user.direccion,user.cellphone,user.email)
        elif(tipo == "estudiante"):
            currentUser = Estudiante(user.userName,user.id,
                user.password,user.nombre,user.edad,user.genero,
                user.direccion,user.cellphone,user.email)
        elif(tipo == "profesor"):
            currentUser = Profesor(user.userName,user.id,
                user.password,user.nombre,user.edad,user.genero,
                user.direccion,user.cellphone,user.email)
        else:
            print("El usuario no existe")
        print(currentUser)


