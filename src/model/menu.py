from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Administrador import Administrador
from src.model.gestionAdmnistrador import *
from src.model.gestionEstudiante import *
from src.model.gestionProfesor import *


def mostrarMenu(nombre, opciones, tipo, currentUser):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'# {nombre}.')
    print(f"{currentUser.nombre} ha ingresado como {tipo}. Seleccione una opción:")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leerOpcion(opciones):
    while (opcion := input('Opción: ')) not in opciones:
        print("Opción incorrecta, vuelva a intentarlo.")
    return opcion

def ejecutarOpcion(opcion, opciones):
    if len(opciones[opcion]) == 2:
        opciones[opcion][1]()
    elif len(opciones[opcion]) == 3:
        a = opciones[opcion][1]
        a(opciones[opcion][2])

def generarMenu(nombre, opciones, opcionSalida, tipo, currentUser):  
    opcion = None
    while opcion != opcionSalida:
        mostrarMenu(nombre, opciones, tipo, currentUser)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        
def menuPrincipal(tipo, currentUser):
    opciones = None
    finalizar = None
    if(tipo == "administrador"):
        finalizar = "6"
        opciones = {
            "1": ("Registrar nuevo usuario.", registrarNuevoUsuario),
            "2": ("Consultar estudiante.", consulta, currentUser),
            "3": ("Actualizar información de usuario.", None),
            "4": ("Asignar asignatura.", incluirAsignatura, currentUser),
            "5": ("Cerrar sesión.", None),
            "6": ("Finalizar el programa.", print, "El programa ha finalizado")
        }
    elif(tipo == "profesor"):
        finalizar = "5"
        opciones = {
            "1": ("Visualizar asignaturas.", None),
            "2": ("Visualizar información personal.", visualizarInfoProfesor, currentUser),
            "3": ("Actualizar información personal.", None),
            "4": ("Cerrar sesión.", None),
            "5": ("Finalizar el programa.", print, "El programa ha finalizado")
        }
    elif(tipo == "estudiante"):
        finalizar = "5"
        opciones = {
            "1": ("Visualizar información personal.", visualizarInfoEstudiante, currentUser),
            "2": ("Actualizar información personal.", None),
            "3": ("Visualizar asignaturas.", None),
            "4": ("Cerrar sesión.", None),
            "5": ("Finalizar el programa.", print, "El programa ha finalizado")
        }
    generarMenu("Menú principal", opciones, finalizar, tipo, currentUser)

    def subMenuConsultarEstudiante():
        opciones = {
            "1": ("Consulta por id: ", ),            
            "2": ("Consulta por nombre", )   
        }

    def submenuactualizarUsuario():
        opciones = {
            "1": ("Consulta por id: ", ),            
            "2": ("Consulta por nombre", )   
        }
    