from src.classes.Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, user, id, psd, nombre, edad, genero, direccion, cnumber, email, asignatura):
        super().__init__(user, id, psd, nombre, edad, genero, direccion, cnumber, email)
        self.agregarAsignatura(asignatura)
    def agregarAsignatura(self,valor):
        self._asignatura = valor