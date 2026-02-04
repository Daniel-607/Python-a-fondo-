print('cadena\tde\tcaracteres\ncon\tseparadores')
print('\t'.join(['a','b','c']))

print('el', 'arbol', 'esta', 'en', 'el', 'bosque')
print('la', 'vaca', 'pasta', 'en', 'el', 'prado', sep='\t', end='...')
print('\nel', 'cespe', 'verde', sep='\n\t', end='\n\n')                                                                                                                                                                                                                                                                                                               

'''Por otro lado se puede definir el stream de datos en el que se pretende escribir. Se puede definir
directamente un fichero y que toda las cadenas se guarden en el o guardalas en los demas streams de datos del sistema 
es decir, el de entrada (sys.stdin) o el de error  (sys.stderr)  veamos un ejemplo '''

f = open('salida.log', 'w')
print('texto', 'por', 'escribir', 'en fichero', file=f)
f.close()
$ cat salida.log
