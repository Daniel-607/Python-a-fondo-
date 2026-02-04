""" a, b = set([1,2,3,4]), frozenset([1,2,3,4,4,4,4])#Se crean conjuntos 
print(b)
print(a) """

#Funciones de actualizacion de conjuntsos 
#operaciones de actualizacion de conjunbtos
setA, setB = {1,2,3,4}, {4,5,6}
setA.add(5)# se Añade 5 a setA
print(setA)

setA.remove(1)#Se remueve el numero 1 de setA si no esta el 1 eleva una excepcion 
print(setA)

setA.discard(1) #elimina el numero 1 de setA y si no esta no eleva ninguna ecepcion 
print(setA)

setA.pop()#elimina y devuelve un elemento arbitrario
print(setA)

setA.clear()#Elimina todo el contenido de setA
print(setA)

setA.update(x for x in range(7))#crea cadenas de caracteres numericas de 0 a 6
print(setA)

setA.difference_update(setB)#elimina los elementos encontrados en setB que esten en setA
print(setA)

clr1 = {'rojo', 'verde', 'negro'}#Usando cadenas de caracteres
clr2 = {'amarillo', 'gris', 'negro'}
clr3 = {'marron', 'ambar', 'verde', 'negro'}

clr1.intersection_update(clr2, clr3)#Mantiene solo los elemento en comun entre CLR2, CLR3 y CLR1
print(clr1)

clr3.symmetric_difference_update(clr2)# ANALIZA TODOS LOS CLR Y MANTIENE LOS ELEMENTOS QUE NO ESTEN EN TODOS A LA VEZ 
print(clr3)