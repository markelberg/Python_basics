class Student:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

std1 = Student("Paco", 32)
std2 = Student("Ana", 36)

print(f"El primer alumno se llama {std1.nombre} y tiene {std1.edad} años")
print(f"La segunda alumna se llama {std2.nombre} y tiene {std2.edad} años")