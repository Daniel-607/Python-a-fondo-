""" >>> f'5*4 = {5 * 4}'
'5*4 = 20'
>>> import datetime
>>> nombre = 'Python'
>>> fecha = datetime.date(2020, 10, 12)
>>> d = dict(cad=['uno', 'dos'])

>>> f'{nombre} en {fecha: %A, %B, %d, %Y} soporta f-strings {d["cad"][1].upper()}'
'Python en  Monday, October, 12, 2020 soporta f-strings DOS' """

"""Creacion de cadenas formateadas en python usandno F-strings"""


 numero, entero = 23.412, 82
>>> nombre1, nombre2 = 'pepe', 'Oscar'
>>> f'{numero}, {entero}, {nombre1}, {nombre2}'
'23.412, 82, pepe, Oscar'


>>> f'Usando conversiones: {nombre2!s}, {nombre2!r}, {nombre2!a}'
"Usando conversiones: Oscar, 'Oscar', 'Oscar'"


>>> f'Usando funciones: {chr(entero)}'
'Usando funciones: R'

>>> f'Usando expresiones: {nombre1 if numero > entero else nombre2}'
'Usando expresiones: Oscar'

>>> f'Usando condicionales: {numero and entero or nombre1}'
'Usando condicionales: 82'

"""Otra razon importante para usar fstrings en vez de otros tipos de formateado es la velocidad de ejecucion
dado que, si se comparan los tiempos de ejecucion de cada tipo, se puede mejora considerable."""

