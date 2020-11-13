
from libro import *

class biblioteca:

    def __init__(self,name):
        self.__name   =   name
        self.__count = 0
        self.__libros = []


    @property
    def name(self):
        return self.__name
        

    @property
    def libros(self):
        lista = []
        for i in self.__libros:
            lista.append(str(i))
        return  lista
                 
        

    @name.setter
    def name(self,name):
        self.__name = name



    def addLib(self,libro):
        if libro in self.__libros:
            print(f'{libro.name} ya está en nuestras estanterias, Prueba con otro BRO 😠 🖐 ')
        else:
            self.__libros.append(libro)
            print(f'{libro.name} se ha añadido a las entanterias, Gracias por su aportación 🙂 😇  ')



if __name__ == "__main__":
    biblio= biblioteca("ULPGC")
    lib1 = libro('Harry Potter','Ruben','Un mago se da leña con todos',['aventura, miedo'])
    lib2 = libro('Harry Potter','JK','Un mago se da leña con todos',['aventura'])
    lib3 = libro('Harry Potter','JK','Un mago se da leña con todos',['aventura'])
    biblio.addLib(lib1)
    biblio.addLib(lib2)
    biblio.addLib(lib3)
    print(biblio.name)
    print(biblio.libros)

    