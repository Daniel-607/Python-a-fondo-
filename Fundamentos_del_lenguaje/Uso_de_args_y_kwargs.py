"""
Alos argumentos posiscioNALES SE LES DENOMINA *ARGS Y A LOS CLAVE VALOR **KWARGS, 

"""
""" 
def mi_funcion(*args, **kwargs):
    print(f'args: {args} kwargs: {kwargs}')

print(mi_funcion())
mi_funcion(42)
mi_funcion(vehiculo = 'Coche')
mi_funcion(456, vehiculo ='Camioin', flag ='activado' ) """
    
"""
Los args y kwargs son muy utiles a la hora de extender clases o de ejecutar muchas funciones que hagan uso de algunos 
parametros que se provean solo en la llamada original, como se muestra a continuacion 
"""

def calculo_general(**kwargs): # esta funcion lo que hace aytravez del **kwargs es resivir cualquier cantidad de parametros 
    ret_s = suma(**kwargs)#se le pide el resultado a la funcion suma y se almacena en ret_s
    ret_d = division(**kwargs)#lo mismo con division 
    return ret_s * ret_d #final mente se retorna la multiplicacion entre los resultados de la funcion suma y resta 

def suma(op1, op2, **kwargs):#si se desea pasar mas parametros la funcion calculo genral los resiviria pero para p[asar mas parametros en el caso de esta funcion se deberia agragar mas parametros si se quiere quer la funcion calculo general reciba mas parametros 
    return op1 +op2

def division(num, deno, **kwargs): # de igual manera sucede con esta funcion 
    return num / deno

res = calculo_general(op1=5, op2=9, num=8, deno=2)
print(res)          

 """
 Los parametros que no aparecen en la definicion de cada funcion, se pueden encontrar en **kwargs dado que por defecto se agragan a ese 
 parametro. Esto permite esto permite agragar tantos parametros clave valor como sea necesario sin que esto afecte el funcionamiento 
 del codigo  
 
 De igual manera, se pueden utilizar parametros posicionales y *arg como se ve en el siguiente ejemplo
 """
 def calculo_posicional(*args):
     ret_s = suma(*args)
     ret_d = division(*args)
     return ret_s * ret_d
 
 def suma(op1, op2 *args):
   return op1 + op2

 def division(a1, a2, num, deno):
    return num / deno
 res = calculo_posicional(5,9,8,2)
 print(res)
 """
 En este ejemplo se puede ver que, al no aceder A los parametros por su clave en la funcion division, hay que agrgar los dos primeros parametros 
 que no se utilizaran dentro de la funcion. 
 
 Por lo general cuando se usa *args **kwargs se hace programacion implicita y no explicita, por lo que se pierde la legibilidad del codigo,
 y se permite que cualquier parametro sea utilizado en todas las funciones, lo que en futuras mopdificaciones del codigo hace muy poco mantenible el mismo 
 por esta razon su uso es delicado y se recomienda nombrar explicitamente los parametros a usar en cada funcion 
 """