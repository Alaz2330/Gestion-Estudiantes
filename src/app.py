from src.classes.Administrador import Administrador
from src.classes.Profesor import Profesor
from src.classes.Estudiante import Estudiante
from src.classes.Usuario import Usuario
from src.util.db import dbSeeder
from src.model.menu import menuPrincipal


def gestionEstudiantes():
    dbSeeder()
    menuPrincipal()


    


    
