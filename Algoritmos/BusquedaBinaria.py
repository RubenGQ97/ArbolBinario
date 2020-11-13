numero = int(input('Dime un numero entre el 0 y el 1000000: '))
min=int(0)
max=int(1000000)
rangoPosible = range(0,1000001)
while True :
    if numero == (max + min)//2:
        min=(max + min)//2
        break
    elif numero > (max + min)//2:
        print( "minimo pasa de: " + str(min) +", a valer minimo="+str((max + min)/2) +",   maximo= "+str(max) )
        min = (max + min)//2
    elif numero < (max + min)/2:
        print( "minimo= " + str(min) +", maximo pasa de valer ="+str(max)+",  a valer maximo= "+str((max + min)/2)  )
        max = (max + min)//2
    
    
print(min)
