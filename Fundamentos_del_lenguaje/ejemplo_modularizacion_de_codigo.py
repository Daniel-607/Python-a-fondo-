"""
Para entender el concepto de modularizacion con funciones se presenta el siguiente ejercicio: partiendo de una cadena de caracteres 
, se pretende separar la cadena medienate un separador y aplicar una funcion basada en el algoritmo de cifrado md5 a cada elemento 
para obtener su forma hexadecimal. Una vez obtenida su forma, se a de guardar en un fichero de texto plano

el algoritmo de cifrado md5 se encuentra en hashlib.md5 de la libreria estandar. para realizar este jercicio se puede usar funciones como las que se muestran a continuacion
"""
import hashlib

def extraer_identificadores(cadena_original, sep''):
    return cadena_original.split(sep)

def aplicar_hash(lst):
    md5s = []
    for cad in lst:
        m = hashlip.md5(cad.encode('utf-8'))
        md5s.append(m.hexdigest())
        return md5s

def escribir_a_fichero(data, nombre_fichero='out.txt'):
    with open(nombre_fichero, ('w')) as f:
        for d in data:
            f.write(d + '/n')
            return nombre_fichero
        
cadena_original = 'texto<>a<>guardar'
identificadores = extraer_identificadores(cadena_original, sep='<>')
id_modificadores = aplicar_hash(identificadores)
nombre_fichero = escribir_a_fichero(id_modificados)

"""
Con este simple ejemplo se puede ver como la logica esta encapsulada en las funciones y no en el nivel principal del modulo. asi se puede
hacer uso de las llamadas a las funciones facilmente 

Ademas, esta la gran ventaja que reprensenta el uso de funciones al mejorar la legibilidad del codigo. Al agrupar seciones de codigo con nombres simples que describen la logica
interna , se puede entender la ejecucion facilmente y facilita que se puedan cambiar partes de la logica de forma trival

su pongamos que a hora cambia la expesificacion del problema de la siguiente forma: se prentende aplicar la funcion de cifrado0 sha256 en vez de md5 y guardar en formato Json 
en vez de texto plano.

Para cumplir con los nuevos requisitos solo es necesario crear unas funciones que sostituyan lo que no se quiere usar a hora...
"""

def aplicar_hash(lst):
        hashes = []
    for cad in lst:
        m = hashlip.sha256()
        m.update(cad.encode('utf-8'))
        hashes.append(m.hexdigest())
        return hashes

def escribir_a_json(data, nombre_fichero='out.json'):
    with open(nombre_fichero, ('w')) as f:
            json.dump(data, f)
            return nombre_fichero
        
cadena_original = 'texto<>a<>guardar'
identificadores = extraer_identificadores(cadena_original, sep='<>')
id_modificadores = aplicar_hash(identificadores)
nombre_fichero = escribir_a_json(id_modificados)

