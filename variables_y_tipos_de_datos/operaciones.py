#Operaciones relacionadas con la codificacdion

'El arbol'.encode('utf-8')
'El qrbol'.encode('ascii')#Este es igual que encode('ascii',errors='strict')
'El qrbol'.encode('ascii', 'replace')
'El qrbol'.encode('ascii', errors='namereplace')
'El qarbol'.encode('ascii', errors='backslashreplace')
'El qarbol'.encode('ascii',errors='xmlcharrefreplace')

""" stric: valor por defecto que intetara hacer la codificacion elegida en el parametro encoding. Si no es posible, eleavra una axcepcio
del tipo ValueError.

ignore: usando esta opciion seignora cualquier error producido

replace: remplaza el caracter mal formado por un (?)

backslashreplace: remplaza el caracter mas formado por su rep[resentacion espacapada usando '\'
                                                              
xmlcharrefreplace: remplaza el caracter mal formado por su referencia apropiada en xml

namereplace: remplaza el car5acter mal formado por su representacion en texto plano unicode \N{...}

Estos valores estan disponibles por defecto pero se pueden usar manejadores de errores propios usando 
la funcion codecs.register_error() """