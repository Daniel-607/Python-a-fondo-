>>> nom, num, nnum, dec, ima = 'arbol', 45, -32.89, 3.562, 4+89j
>>> #Alineacion y relleno de cadenas (aling y fill)
>>> f'{nom:_<15} - {num:_=15} - {dec:_^15} - {ima:_>15}'
'arbol__________ - _____________45 - _____3.562_____ - ________(4+89j)'
>>> f'{nom:<15} - {num:=15} - {dec:^15} - {ima:>15}'
'arbol           -              45 -      3.562      -         (4+89j)'
>>>
>>> #Expresando los signos de los numeros
>>> f'{num:+} , {num: } , {nnum:-} , {nnum:}'
'+45 ,  45 , -32.89 , -32.89'
>>>
>>> #Añadiendo _y , para separar los numeros grandes
>>> gran_numero = 2341526321.234
>>> f'{gran_numero:<30} {gran_numero>30,}'
'2341526321.234                 (True,)'
>>> f'{gran_numero:<30} {gran_numero:>30,}'
'2341526321.234                              2,341,526,321.234'
>>>
>>> #Usando la notacion alternativa
>>> f'Anotacion alternativa {452:#b} {452:#o} {452:#x}'
'Anotacion alternativa 0b111000100 0o704 0x1c4'
>>>
>>> #Añadiendo la presicion o limitando el numero de caracteres
>>> f'{14.36146:.4} - {"casa de papel":.6}'
'14.36 - casa d'
>>>
>>> #Expresando valores en diferentes formatos segun el tipo
>>> f'Entero en cadena {6342}'
'Entero en cadena 6342'
>>> f'Entero binario {6342:b}'
'Entero binario 1100011000110'
>>> f'Entero a caracter {1234:c}'
'Entero a caracter Ӓ'
>>> f'Entero a decimal {160:d}'
'Entero a decimal 160'
>>> f'Entero a Octal {1345:o}'
'Entero a Octal 2501'
>>> f'Entero a hexadecimal {15:x}'
'Entero a hexadecimal f'
>>> f'Entero a hexadecimal {160:x} mayusculas'
'Entero a hexadecimal a0 mayusculas'
>>> f'Entero a hexadecimal {160:X} mayusculas'
'Entero a hexadecimal A0 mayusculas'
>>> f'Entero y punto flotante como punto flotante {541562761:f}'
'Entero y punto flotante como punto flotante 541562761.000000'
>>> f'Entero y punto flotante como punto flotante {541562761:f} {12.34154256:F}'
'Entero y punto flotante como punto flotante 541562761.000000 12.341543'
>>> f'Entero y float como notacion cientifica {541562761:e} {12.34154256:E}'
'Entero y float como notacion cientifica 5.415628e+08 1.234154E+01'
>>> f'porcentaje {342:%} {12.345:%}'
'porcentaje 34200.000000% 1234.500000%'

'''El mini lenguaje de formateo de strings en python define como presentar valores dentro
de f-strings o format(). va despues de dospuntos: dentro de {}

ejuemplo f"{}valor:spec"
estructura general  [[fill]aling [sign][#][0][width][grouping][.precision][type]]

ALINEACION Y RELLENO
'''
f"{'hola':>10}" #'      hola' (derecha)
f"{'hola':<10}"#'hola   '(Izquierda)
f"{'hola':^10}"#'   hola  '(Centrado)
f"{'hola':*^10}"#'*****hola*****'

"""SIGNOS PARA NUMEROS"""
f"{42:+}"#'+42'
f"{42:-}"# '42'
f"{42: }"# ' 42'(Espacio si es positivo)

"""Ancho minimo """
f"{99:6}"#'     99'

"""Agrupacion de miles"""
f"{1000000:,}"#'1,000,000'
f"{1000000:_}"#'1_000_000'

"""Presicion de decimales o digitos significativois"""
f"{3.14159:.2f}"#'3.14'
f"{3.14159:.3}"#'3.14'

""" Tipo smas comunes 
d = decimal
b = binario
o = octal
x = hexadecimal en minuscula
X = hexadecimal en mayuscula

FLOTANTES
f = punto fijo
e = notacion cientifica
g = formato general
% = porcentaje
"""