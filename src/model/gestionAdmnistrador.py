from src.classes.Profesor import *
from src.classes.Estudiante import *
from src.classes.Administrador import *

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
