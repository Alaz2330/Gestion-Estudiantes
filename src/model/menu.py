from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador
from src.model.login import login
from src.model.gestionAdmnistrador import *


tipo, user = login()
def mostrarMenu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'# {nombre}.')
    print(f"{user.nombre} ha ingresado como {tipo}. Seleccione una opción:")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leerOpcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutarOpcion(opcion, opciones):
    if len(opciones[opcion]) == 2:
        opciones[opcion][1]()
    elif len(opciones[opcion]) == 3:
        consulta(user)

def generarMenu(nombre, opciones, opcionSalida):  
    opcion = None
    while opcion != opcionSalida:
        mostrarMenu(nombre, opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        
def menuPrincipal():
    opciones = None
    finalizar = None
    if(tipo == "administrador"):
        finalizar = "6"
        opciones = {
            "1": ("Registrar nuevo usuario.", registrarNuevoUsuario),
            "2": ("Consultar estudiante.", consulta, user),
            "3": ("Actualizar información de usuario.", None),
            "4": ("Asignar asignatura.", None),
            "5": ("Cerrar sesión.", None),
            "6": ("Finalizar el programa.", None)
        }
    elif(tipo == "Profesor"):
        finalizar = "6"
        opciones = {
            "1": ("Visualizar asignaturas.", None),
            "2": ("Visualizar información personal.", None),
            "3": ("Actualizar información personal.", None),
            "4": ("4. Asignar asignatura.", None),
            "5": ("Cerrar sesión.", None),
            "6": ("Finalizar el programa.", None)
        }
    elif(tipo == "Estudiante"):
        finalizar = "5"
        opciones = {
            "1": (" Visualizar información personal.", None),
            "2": ("Actualizar información personal.", None),
            "3": ("Visualizar asignaturas.", None),
            "4": ("Cerrar sesión.", None),
            "5": ("Finalizar el programa.", None)
        }
    generarMenu("Menú principal", opciones, finalizar)

    def subMenuConsultarEstudiante():
        opciones = {
            "1": ("Consulta por id: ", ),            
            "2": ("Consulta por nombre", )   
        }


