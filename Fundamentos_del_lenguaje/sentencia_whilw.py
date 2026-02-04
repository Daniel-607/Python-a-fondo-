""" i=0
while i < 5:
    print(f'Iteracion {i}') #la f dentro del print indica que la cadena es un f - string lo cual permite insertar variables dentro del texto sin necesidad de concatenar 
    i += 1
else:
    print(f'i ya es mayor que 5')"""
    
en_bucle = True 
while en_bucle:
    x = int(input('Por favor ingrese un numero:'))
    if x > 0:
        print(f'El numero {x} es positivo')

    elif x < 0:
        print(f'El numero {x} es negativo')  
    elif x == 0:
        en_bucle = False
else:
    print('Ejecucion termino')