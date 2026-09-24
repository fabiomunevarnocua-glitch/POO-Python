
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

pedro = Estudiante("Pedro", 15, "10°")

print("Nombre:", pedro.nombre,", edad:", pedro.edad, ", grado:", pedro.grado)


