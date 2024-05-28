from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador

def registrarNuevoUsuario():
    while True: 
        tipo = input('''Ingrese el tipo:
                1) Administrador
                2) Profesor
                3) Estudiante
                ''')
        if tipo in ['1', '2', '3']:
            break  
    atributos = {"id":"el número de identificación","password":"la contraseña","userName":"el usuario", 
            "nombre":"el nombre", "edad":"la edad", "genero":"el genero", "direccion":"la direccion de residencia", 
            "cellphone":"el número de celular", "email":"el email"
    }
    for llave in atributos:
        atributos[llave] = input(f"Ingrese {atributos[llave]}:")
        
    if tipo == "1":
        administrador = Administrador(atributos["id"],atributos["userName"],atributos["password"],atributos["nombre"],atributos["edad"],atributos["genero"],atributos["direccion"],atributos["cellphone"],atributos["email"])
        administrador.crearUsuario()
    elif tipo == "2":
        profesor = Profesor(atributos["id"],atributos["userName"],atributos["password"],atributos["nombre"],atributos["edad"],atributos["genero"],atributos["direccion"],atributos["cellphone"],atributos["email"])
        profesor.crearUsuario()
    elif tipo == "3":
        estudiante = Estudiante(atributos["id"],atributos["userName"],atributos["password"],atributos["nombre"],atributos["edad"],atributos["genero"],atributos["direccion"],atributos["cellphone"],atributos["email"])
        estudiante.crearUsuario()

def consulta(currentUser):
    users = ()
    identificador = input("Ingrese el id o el nombre del estudiante: ")
    users = currentUser.consultarEstudiante(identificador)
    if users == (None) or len(users) == 0:
        print("No se han encontrado coincidencias.")
    else:
        for data in users:
            print (data.mostrarUsuario())
            

def actualizarUsuario(currentUser):
    while True:
        print(
        '''Ingrese el tipo de actualización que desea realizar:
        1) Actualizar información personal.
        2) Actualizar información de otro usuario.
        '''    
        )
        opcion = input()
        if opcion in ["1", "2"]:           
                break
    if opcion == "2":
        atributos = {"password":"la contraseña", "nombre":"el nombre", 
                    "direccion":"la direccion de residencia", 
                    "cellphone":"el número de celular", "email":"el email"
        }
        numero = 1
        print("Ingrese el tipo de dato que desea actualizar")
        for llave in atributos:
            numero += 1
            print(f"{numero}) {atributos[llave]}.")
        #while True:

        #input()


        #atributos[llave] = input(f"Ingrese {atributos[llave]}:")
        #atributo = input()
        #valor = input()

def incluirAsignatura(currentUser): 
    nombre = input("Ingrese el nombre de la asignatura: ")    
    users = currentUser.consultarProfesores()   
    numero = 1
    print("A continuación se mostrará la lista de profesores:")
    for user in users:
       print(f"{numero}) ID: {user.id} Nombre: {user.nombre}")
       numero += 1 
    profesorId = ""
    while profesorId == "":
        indice = input("Ingrese el numero de indice del profesor a añadir: ")
        if int(indice) >= 1:
            user = users[int(indice)-1]
            profesorId = user.id
    currentUser.crearAsignatura(nombre, profesorId)
        

        



