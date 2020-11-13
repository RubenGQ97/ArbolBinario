import random as rd


def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j] , lista[j+1] = lista[j+1], lista[j]
    return lista



if __name__ == "__main__":
    
    tamano = int(input("Dime tamaño de la lista :"))

    lista = [rd.randint(0,1000) for i in range(tamano)]
    print(f'\n\nLista sin ordenadas:\n{lista}')
    burbuja(lista) 
    print(f'\n\nLista sin ordenadas:\n{lista}')