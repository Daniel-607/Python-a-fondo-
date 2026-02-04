>>> b'\x79\x123\x20'
b'y\x123 '
>>> br'\x79\x123\x20'
b'\\x79\\x123\\x20'

>>> br'\x79\x20' #Al utilizar el prefijo r, la cadena no se construye interpretando los caracteres hexadecimales como en el ejemnplo anterior
b'\\x79\\x20'
>>> a = br'\x79\x20'

>>> a.hex('_',2)
'5c78_3739_5c78_3230'
