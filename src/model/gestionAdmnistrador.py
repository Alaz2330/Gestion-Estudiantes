from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador
from src.classes.Usuario import Usuario

def registrarNuevoUsuario():
    while True: 
        tipo = input('''Ingrese el tipo:
                1) Administrador.
                2) Profesor.
                3) Estudiante.
                ''')
        if tipo in ['1', '2', '3']:
            break  
        else:
            print("Opción incorrecta, vuelva a intentarlo.")
    atributos = {"id":"el número de identificación",
                 "password":"la contraseña",
                 "userName":"el usuario", 
                 "nombre":"el nombre", 
                 "edad":"la edad", 
                 "genero":"el genero", 
                 "direccion":"la direccion de residencia", 
                 "cellphone":"el número de celular", 
                 "email":"el email"
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
            print (data.mostrarUsuarioAdministrador())
            

def actualizarUsuario(currentUser):
    while True:
        print(
        '''Ingrese el tipo de actualización que desea realizar:
        1) Actualizar información personal.
        2) Actualizar información de otro usuario.    
        3) Volver al menu principal.
        '''    
        )
        opcion = input("Opción: ")
        if opcion in ["1", "2", "3"]:           
                break
        else:
            print("Opción incorrecta, vuelva a intentarlo.")
    if opcion == "1":
        userName, id, password, nombre, edad, genero, direccion, cellphone, email = currentUser.mostrarUsuarioAdministrador()
        atributos = {"password": (f"La contraseña: {password}"), 
                     "nombre":(f"El nombre: {nombre}"),
                     "direccion":(f"La direccion de residencia: {direccion}"), 
                     "cellphone":(f"El número de celular: {cellphone}"), 
                     "email":(f"El email: {email}")
                }       
        while True:
            print("Seleccione el tipo de dato que desea actualizar")
            numero = 1
            for llave in atributos:            
                print(f"{numero}) {atributos[llave]}.")
                numero += 1
            opcion2 = int(input("Opción: "))
            if opcion2 in range(1,6):   
                listatributos = list(atributos.keys())
                atributo = listatributos[opcion2-1]
                valor = input("Ingrese el dato actualizado")
                currentUser.actualizarUsuario(atributo, valor)                                 
            else: 
                print("Opción incorrecta, vuelva a intentarlo.")                
    #if opcion == "2":

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
        

        



