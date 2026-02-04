#Caracteres ascii La función map() aplica la función lambda a cada carácter de la cadena.
#El resultado será un iterador de valores booleanos:La función all() devuelve True si todos los elementos del iterable son True.
#En este caso:
all(map(lambda x: x.isascii(), 'abc}~?'))
any(map(lambda x: x.isascii(), 'ñ¿'))#caracteres no ascii
