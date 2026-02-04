tipo = 'coche'
if tipo == 'coche':
    ruedas = 4
elif tipo == 'bicicleta':
    ruedas = 2
elif tipo == 'camion':
    ruedas = 6
else:
    ruedas = -1
 
tipo_a_ruedas = {'coche':4, 'bicicleta':2, 'camion':6}
ruedas2 = tipo_a_ruedas.get(tipo,-1)   
