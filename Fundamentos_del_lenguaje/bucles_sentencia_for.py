
for x in range(10):
    if x > 2 and not x % 2: # esta linea de codigo solo permite imprimir valores de x que sean mayores que 2 y ademaS PARES 
        print(x)
else:
    print('Fin de la evaluacion')
    

for nombre_eq, punt in [('Equipo 1', 89), ('Equipo 2', 123)]:# el cilclo for atravez del in acede a cada tupla y asigna los valores de cada tupla a cada variable cuando el in no encuentra mas tuplas se detiene el ciclo for
    print(f'{nombre_eq}: {punt}')
    
a = [1,2,3,4,5,6]
for x in a:
    a.remove(x) #al eliminar una lista mientras se itera sobre ella los indices de los elementos restantes cambian  
print(a)
a = [1,2,3,4,5,6]
for x in a:
    a.append(x+100)#Provoca un bucle infinito al añadir elementos sin  parar ya que en cada iteracion se añade a lista un nuevo valor en este caso 100
  
#Si por el contraio se utiliza un diccionario para iterar sobre el y se intenta camboiar el tamaño deol mismo durante la ejecucion del bucle, se elevarauna excepxion del tipo RunTimeError

d = dict(uno=1,dos=2,tres=3)
for k, v in d.items(): #items lo que hace es que devuelve cada clave del dicionario atravez del operador in 
    del d[k] # esto elimina cada una de las claves en cada iteracion lo cual es un error 

#Los de arriba son algunos de los ejemplos de las com=nsecuencias de cabiar el tamaño de iterador mientras se ejacutando un bucle for por lo que se recomienda que
#, si se pretende cambiar el valor del objceto a iterar se haga previamente una copia del mismo y se itere sobre ella 

a = [1,2,3,4,5,6]
 for in a[:]:#Creando copia de a usando :
     a.append(x + 100)
print(a)

d = dict(uno=1, dos=2, tres=3)
dd = d.copy()
for k, v in dd.items()
     del d[k]