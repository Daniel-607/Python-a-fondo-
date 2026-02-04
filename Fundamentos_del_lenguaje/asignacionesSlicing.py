
>>> lst = [1,2,3,4,5,6] #se crea una lista 
>>> a,*b,c=lst # *b lo que hace es que captura los valores sobrantes de la lista y los alamacena en una lista propia 
>>> a
1
>>> b
[2, 3, 4, 5]
>>> c
6
>>> d,e,f = lst[0],lst[1:-1], lst[-1] #lst[1:-1] es una operacion llamada slicing o rebado de lista hace basicamente lo mismo que *b en la linea 2
>>> d,e,f
(1, [2, 3, 4, 5], 6)
>>> a == d, b == e, f == c
(True, True, True)
>>>