from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador

def registrarNuevoUsuario():
    while True: 
        tipo = input('''Ingrese el tipo:
                1. Administrador
                2. Profesor
                3. Estudiante
                ''')
        if tipo in ['1', '2', '3']:
            break  
    atributos = {"userName":"el usuario","id":"el número de identificación","password":"la contraseña", 
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

def consulta(user):
    users = ()
    while True:
        opcion = input('''Ingrese el tipo de consulta
                                1)Consulta por id.            
                                2)Consulta por nombre. 
                                ''')
        if opcion in ["1", "2"]:           
            break
    if opcion == "1":
        identificador = input("Ingrese el id del estudiante: ")
        users = user.consultarEstudiante(identificador)
    elif opcion == "2":  
        identificador = input("Ingrese el nombre del estudiante: ")
        users = user.consultarEstudiante(identificador)
    #elif opcion == "3":
        #identificador = input.upper("Ingrese el nombre de la asignatura: ")
        #user.consultaEstudiante(identificador)
    for data in users:
        data.mostrarUsuario()
    
    



