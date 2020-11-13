

class libro:

    def __init__(self, name, autor, sinapsis,generos):
        self.__name = name
        self.__autor = autor
        self.__sinapsis = sinapsis
        self.__generos= generos
    

    @property
    def name(self):
        return self.__name

    
    @property
    def autor(self):
        return self.__autor


    @property
    def sinapsis(self):
        return self.__sinapsis


    @property
    def generos(self):
        return self.__generos


    def __eq__ (self,other):
        return self.autor == other.autor and self.name == other.name


    def __str__ (self):
        return f'{self.name}:   Autor: {self.autor}     Generos{self.generos}'

