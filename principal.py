from paquete1.modelo import *
#Creación de objetos tipo docente, en este caso dos docentes
d = Docente("Docente: B.D", "Loja")
d2 = Docente("Docente: Programación", "Quito")
#Creacion de lista de docente, usando a d y d2
listado = [d,d2]
#Creacióm de objeto tipo estudiante
e = Estudiante("Luis", listado)
#presentacion
print("")
print("EJERCICIO TUTORIA: 3")
print(e.presentar_datos())