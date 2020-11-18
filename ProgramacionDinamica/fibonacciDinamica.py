#Funcion de fibonnaci realizado con programación dinámica.
import sys

def Fibonacci_Dinamico (number, memory):
    if number == 0 or number == 1:
        return 1
    
    try:
        return memory[number]
    except KeyError:
        result= Fibonacci_Dinamico(number - 1, memory) + Fibonacci_Dinamico(number - 2, memory)
        memory[number]=result
        return result


if __name__ == '__main__':
    sys.setrecursionlimit(1000000000)
    memory={}               #Para prueba, normalmente seria propio del metodo
    while True:
        number=int(input("Ingresa un número: "))
        Fibonacci_Dinamico(number,memory)
        print(f'El resultado es {memory[number]}')

    


