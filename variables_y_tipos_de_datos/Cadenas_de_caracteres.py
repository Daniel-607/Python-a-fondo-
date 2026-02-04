str()

#Asiganacion de variables por empaquetado c es un tipo de dato complexe es un tipo de dato float 
a, b, c, e = 23, 3.45, 2-3J, 8.56e+12
#se convierte cada objecto en su representacion en cadena str 
str(a), str(b), str(c), str(e)
import datetime
#Crea un objeto datetime para el 8 de mayo de 2020 a las 05:35 y lo convierte a cadena.
#Resultado típico: '2020-05-08 05:35:00' (formato YYYY-MM-DD HH:MM:SS)


str(datetime.datetime(2020, 5, 8, 5, 35))
#Aqui se convierte una cadena de texto(piraña) en una cadena de bytes Resultado: b'pira\xc3\xb1a'
'piraña'.encode()
#interpreta estos bytes como si estuvieran codificados en UTF-8 y conviértelos a texto
str(b'Pira\xc3\xbla', encoding='utf-8')

str(b'Pira\xc3\xbla', encoding='latin-1')
str(b'Pira\xc3'\xbla')
"b'Pira\\xc3\\xbla'"
str(b'Pira\xc3\xbla', encoding='ascii', errors='replace')
str(b'Pira\xc3\xbla', encoding='ascii', errors='backslashreplace')
str(b'Pira\xc3\xbla', encoding='ascii', errors='ignore')
    