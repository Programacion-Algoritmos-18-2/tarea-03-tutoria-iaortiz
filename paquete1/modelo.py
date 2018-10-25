#Creación de clase docente
class Docente :
    def __init__ (self, n, a):
        self.nombre = n
        self.ciudad = a
    # Metodo get y set para nombre
    def agregar_nombre (self, n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre

    # Metodo get y set para ciudad
    def agregar_ciudad (self, a):
        self.ciudad = a
    def obtener_ciudad(self):
        return self.ciudad
    #Presentación
    def presentar_datos (self):
        cadena = "%s\n\t%s" %(self.obtener_nombre() , self.obtener_ciudad())
        return cadena
#Creación de clase estudiante
class Estudiante:
    def __init__ (self,n,listaDocentes):
        self.nombre = n
        self.docente = listaDocentes
    #Metodo get y set para nombre
    def agregar_nombre (self , n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre

    # Metodo get y set para lista docente
    def agregar_listaDocentes(self, listaDocentes):
        self.docente = listaDocentes
    def obtener_listaDocentes(self):
        return self.docente

    #Método de presentación de datos
    def presentar_datos(self):
        cadena = "Estudiante: %s\n" % (self.obtener_nombre())
        #Variable que concatena el encabezado
        cadena = "%s%s\n" % (cadena,"Lista de docentes")
        #Ciclo for para recorrer la lista de docentes
        for i in self.obtener_listaDocentes():
            #Variable cadena con concatenación del encabezado y la presentación con los docentes
            cadena = "%s\n%s" %(cadena, i.presentar_datos())
        return cadena