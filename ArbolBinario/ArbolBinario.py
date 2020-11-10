
import random as rd


class Node:
    
    def __init__ (self):
        self.left = None
        self.right =  None
        self.value = None


    def getLeft(self):
        return self.left


    def getRight(self):
        return self.right
    

    def add(self,value):
        if self.value == None:
            self.value = value
            self.left = Node()
            self.right = Node()
            
        elif self.value > value:
            self.left.add(value)
        else:
            self.right.add(value)





def contains(arbol,number):
    """
    Recibe por parametro el arbol binario y un valor.
    Se devuelve True se el valor ya se encuentra en el arbol y False en caso contrario.

    """

    if arbol.value == None:
        return False
    if arbol.value == number:
        return True
    elif arbol.value > number:
        return contains(arbol.left,number)
    else:
        return contains(arbol.right,number) 
    

def showInOrder(arbol, lista):
    """
    Recibe por parametro el arbol binario y una lista vacia.
    Se devuelve la misma lista pero con los elementos del arbol ordenados.

    """
    
    if arbol.value == None:
        return None
    showInOrder(arbol.left,lista)
    lista.append(arbol.value)
    showInOrder(arbol.right,lista)
    


if __name__ == "__main__":
    arbol = Node()
    lista = []
    for i in range(50):
        number = rd.randrange(0,1000)
        if contains(arbol,number) == False:
            arbol.add(number)
            print( f"se inserta {number} " )
        else:
            print(f"se intentó añadir {number} pero ya se encuentra en la lista")

    showInOrder(arbol,lista)
    print("\n\nLista ordenada:\n")
    for i in lista:
        print(i)