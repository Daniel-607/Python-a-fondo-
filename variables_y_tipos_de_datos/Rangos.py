inicio, final, paso=5, 10, 2
range(final)
list(range(final))
list(range(inicio, final))
list(range(inicio, final, paso))
list(range(-10, 5))
list(range(-10, 14, 3))
list(range(6, -12, -2))

#L as operaciones so[portadas por los rangos son las siguientes (rang1 hace refrenecia a un objecto tipo range 
# y num, a un entero)
rang1 =range
num = 4
rang1.count(num) # devuelve el numero de concurrencias de numen el rango. segun la naturaleza del tipo range 
#solamente se tiene una ocurrencia, o ninguna, de cada numero entero
rang1.index(num)#Devuelve el indice donde se encuentra el numero num dentro del rango sino esta presente 
#eleva una excepcion de tipo valuer error 
rang1.start#es un atributo que permite consultar el numero en el que comieza el rango
rang1.step#es una atributo que permite consultar el paso numerico usado en el rango 
rang1.stop#es un atributo que permite consultar el numero maximo en el que el rango parara 

#EJEMPLOS 
inicio1, final1, paso1 =5, 10, 2
x = range(inicio1, final1, paso1)
x.start, x.stop, x.step
x.index(7)
x.count(6)
x.count(9)
list(x)
  
