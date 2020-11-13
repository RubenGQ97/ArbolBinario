import random as rd


def mergeSort(lista):
    n=len(lista)
    if  n > 1:
        mitad = n //2
        left = lista[:mitad]
        right = lista[mitad:]

        mergeSort(left)
        mergeSort(right)


        i=0
        j=0
        k=0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                lista[k] = left[i]
                i+=1
            else:
                lista[k] = right[j]
                j+=1
            k+=1
        while len(left) > i:
            lista[k] = left[i]
            k+=1
            i+=1
        while len(right) > j:
            lista[k] = right[j]
            k+=1
            j+=1
        
    return lista



if __name__ == "__main__":
    
    tamano = int(input("Dime tamaño de la lista :"))

    lista = [rd.randint(0,1000) for i in range(tamano)]
    print(lista)
    mergeSort(lista)
    print(lista)