from paquete1.modelo import *
#se crea los objetos
d = Docente("Docente B.D", "Loja")
d2 = Docente("Docente Pray", "Quito")
#Creacion de listas
listado = [d,d2]
e = Estudiante("Luis", listado)
#presentacion
print(e.presentar_datos())