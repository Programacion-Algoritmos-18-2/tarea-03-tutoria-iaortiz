class Docente :
    def __init__ (self, n, a):
        self.nombre = n
        self.ciudad = a
    def agregar_nombre (self, n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre
    def agregar_ciudad (self, a):
        self.ciudad = a
    def obtener_ciudad(self):
        return self.ciudad
    def presentar_datos (self):
        print("Docente")
        cadena = "%s\n\t%s" %(self.obtener_nombre() , self.obtener_ciudad())
        return cadena

class Estudiante:
    def __init__ (self,n,listaDocentes):
        self.nombre = n
        self.docente = listaDocentes
    def agregar_nombre (self , n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre
    def agregar_listaDocentes(self, listaDocentes):
        self.docente = listaDocentes
    def obtener_listaDocentes(self):
        return self.listaDocentes
    def presentar_datos(self):
        cadena = "Estudiante: %s\n" % (self.obtener_nombre())
        cadena = "%s %s\n" % (cadena,"lista_docentes")
        for x in range(0, len(self.docente)):
            cadena = "%s\n\t-%s|%s" %(cadena, self.docente[x].obtener_nombre(), self.docente[x].obtener_ciudad())
        return cadena