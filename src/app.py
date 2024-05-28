from src.classes.Administrador import Administrador
from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Usuario import Usuario
from src.util.db import dbSeeder
from src.model.menu import menuPrincipal
from src.model.login import login


def gestionEstudiantes():
    dbSeeder()
    while True:        
        tipo, user = login()
        if tipo != None and user != None:
            menuPrincipal(tipo,user)


    


    
