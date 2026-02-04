>>> 'Representando numeros {}, {} y {}'.format(1,2,3)
'Representando numeros 1, 2 y 3'
>>> 'Repitinedo elementos {0}-{2}-{0}-{1}'.format('a','b','c')
'Repitinedo elementos a-c-a-b'
>>> 'Acediendo a listas {0[0]} {1[1]}'.format([1,2],[2,3])
'Acediendo a listas 1 3'
>>> 'Numero real {0} parte real: {0.real} y parte imaginaria: {0.imag}'.format(5 - 4j)
'Numero real (5-4j) parte real: 5.0 y parte imaginaria: -4.0'

""" ''' Como se puede observar en los ejemplos, se utilizan principalmente los caracteres '{'y'}'
para definir el hueco donde iria un objecto que se pasa como parametro en la funcion.   No obstante, se 
puede espesificar exactamente el numero de posiciones del objecto que se quiere situar en ese hueco, acceder a un metodo del objecto o incluso reutilizar 
cualquier argumento m7ultiples de veces.''' """

#Otra opcion es utilizar nombres nombres como clave, tanto como paramnetro
#dentro de la plantilla como en el siguiente ejemplo 
>>> 'Tipo de vehiculo {c_type}, numero de ruedas {n_ruedas}'.format(c_type='coche', n_ruedas=4)
'Tipo de vehiculo coche, numero de ruedas 4'

"""Esta funcion es muy util cuando se quiere generar cadenas de caracteres dinamicas basadas en codigo que 
cambia en tiempo de ejecucion, por lo que no se puede espesificar como una cadenas estatica en el codigo fuentes 
existe un tipo de cadena de caracteres introducida en python 3 llamada F-STRING, que tiene la finalidad 
de simplificar la sintaxis del formateado.

tambien existe una forma mas antigua de formatear cadenas de caracteres que hace uso de '%' tanto en la plantilla 
como a la hora de pasar los argumentos que se quieren anadir soporta muchas funcionalidades que soporta format , aunque no todas, y es menos potentente 
que el nuevo formato f-format, por lo que su uso esta en declibe.

Con este formato se pueden pasar elemnetos a la cadena que se utiliza como plantilla de forma posicional o haciendo uso de un dicionario.
"""
>>> '%(nombre)s tiene %(numero)02d tipos de comillas'% {'nombre': 'Python', 'numero': 2}
'Python tiene 02 tipos de comillas'
>>> 'Hay %d %s por la carretera' % (4,'coches')
'Hay 4 coches por la carretera'

"""La funcion format_map  es similar a format, pero requiere de un diccionario como parametro y no hace copias internas del mismo. 
Es muy util cuando se pretende representar un dicionario- o las variables de una parte de codigo con locals()
de forma ordenada y sin hacer copias del mismo """

'vehiculo tipo: {v_type} con {n_ruedas} ruedas'.format_map(locals())
'vehiculo tipo: coche con 4 ruedas'
>>> 'El arbol mide {diametro}cm de diametro y {alto}m de alto'.format_map(dict(diametro=54, alto=5))
'El arbol mide 54cm de diametro y 5m de alto'