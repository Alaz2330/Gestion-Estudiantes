class Asignatura:
    def __init__(self, nombre, profesor, notas = None):
        self.nombre = nombre
        self.profesor = profesor 
        self.agregarNotas = notas
    def agregarNotas(self,valor):
        self._agregar = valor