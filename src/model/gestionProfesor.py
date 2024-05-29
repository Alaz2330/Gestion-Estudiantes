from src.classes.Profesor import Profesor


def visualizarInfoProfesor(currentUser):
    print(currentUser.mostrarUsuario())

def asignarNota(currentUser):
    currentUser.consultarAsignatura()
    print(f"asignaturas[0]")
