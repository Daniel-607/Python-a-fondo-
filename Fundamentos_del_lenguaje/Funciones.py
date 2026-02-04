def foo():
    pass #No define logica, solo una funcion con nombre foo

def menor_valor(iter):
    return min(iter)

menor_valor([1,2,3,4])
print(menor_valor())#Esto daria como resultado el nu8mero 1 

menor_valor(range(4))
print(menor_valor())#Esto daria como resultado el 0

menor_valor(['Juan', 'Ana', 'Maria'])
print(menor_valor())# Esto devuelve ana ya que cuando trabajamos en python cadenas de texto con la funcion min() este las organiza en orden alfabetico 

def iniciales(cadena, sep=''):#DEvuelve las iniciales de cada palabra en la cadena separadas por sep 
    return ''.join([x[0].upper() for in cadena.split(sep)])
iniciales('Juan Perez Martinez')
print(iniciales)

iniciales('En una ciudad de la mancha de cuyo nombre no quiero acordarme')
print(iniciales)

iniciales('el,arbol,del,parque', sep=',')
print(iniciales)

a = 'Hola'
b = 'Mundo'




def suma(elem1, elem2):
    elem1 += elem2
    return elem1

c = suma(a,b) #Al ser objectos No mutables, a nose modifica
print(c)#'Hola Mundo'
print(a)#'HOLA'
print(b)#'Mundo'

a = [1,2,3]
b = [4,5]
c = suma(a,b)
print(c)#Imprime la suma de las dos listas 
print(a)#Al ser a un objecto mutable, se a modificado a
print(b)#Este no se modifico 
"""
segun este ejemplo anterior hay que tner en cuenta la mutabilidad de las varariables a la hora de trabjar con ellas dentro de las funciones
cuando se usan valores por defectoen las funciones, hay que tener especial precaucion de que estos no sean de tipo mutable. se recomienda 
cambiarlos por none y compro9bar si el valor como ar=gumentop es none para inicializar como en el sigueinte ejemplo 

"""
def añadir_valor(elem, lst=[]):#ERROR No usar objectos mutables ([]) para valores por defecto de funciones 
    lst.append(elem)
    return lst
añadir_valor(1)
añadir_valor(5)
añadir_valor(2)

def añadir_valor_seguro(elem, lst=None):#Valor por defecto correcto
    if lst is None:
        lst = []
        lst.append(elem)
        return lst

añadir_valor_seguro(1)
añadir_valor_seguro(5)
