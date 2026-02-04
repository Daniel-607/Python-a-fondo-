a = [9, 9, 6]#similar a list([9, 9, 6])
a.append(34.21)#Anade un dato al final de la lista en este caso 34.21
b=list(range(4))#Creacion de lista usando iteRABLE RANGE [0, 1, 2, 3]
a.extend(b)#Uniendo o extendiendo a con lista b 
a.extend(3)#Extendiendo a con iterable rango 3
a.count(2)#numero de concurrencias del numero 2 cuantAS VESCES ESTE EL NUMERO 2
a.index(2)#indice del pri8mer elemento 2
a.index(2, 7)#Indice del elemento 2 contando desde la posicion 7
b.clear()#se eliman los datos de b 
a.insert(0,'pepe')#En la posicion 0 ingrese el nombre pepe
a.insert(3,'Juan')
a.pop(4)#Muestra lo que hay en la posicion 4
a.pop()#Muestra la ultima posicion
a.remove(2)#remueve lo que hay en la posicion 2
a.reverse()#modifica los valores en orden contrario 
xs = [[1, 2, 3], ['Juan', 'ana'],True]
ys =xs.copy # usando la funcion copy sobre listas solo se hace una copia superficial, por lo que los elementos
#mas alla, del primer nivel como puede ser una lista dentro de una lista no se copian como copias sino 
#como referencias esto hace que realmente sigan estando enlazadas entre si 

#sin embargo si se utiliza la funcion que copie en pronfundidad como 
#copy.deepcopy, este problema desaparece

import copy
import sys
yys = copy.deepcopy(xs)
#para conocer el espacio que ocupa un objecto en memoria se puede utiulizar 
sys.getsizeof(a)#Cuanto espacio en memoria ocupa la lista a
#Parta eliminar cualquier objectoy en particulucalar cual quier elemento de una lista
del x[0]#Elimine de el objecton ubicado en la posicion 0 de la lista
del x[1:3]#Elimine los objectos ubicados en la posicion 1 y 3 de la lista 

