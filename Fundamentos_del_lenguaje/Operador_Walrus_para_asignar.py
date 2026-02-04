#Sin usar Walrus
""" 
n = range(5)
len_n = len(n)
if len_n > 2:
    print(f'{len_n} es mayor que 2')
block = f.read(256)
while block != '':
    process(block)
    block = f.read(256)
    [chr(x) for x in range(0x1100) if chr(x).isnumeric()] """
    

""" n = range(5)
if (len_n := len(n)) >2:# en esta linea de codigo lo que hacemos es simplificar atraves del operador walrus ya que este permite calcular la lopngitud de la variable n y asu ves sompararla 
    print(f'{len_n} es mayor que 2')


while (block := f.read(256)) != '':
    process(block)

[c for x in range(0x1100) if (c := chr(x).isnumeric())] """

#Otro ejemplo podria ser utilizando la sentencia is elif como se ve a comtinuacion 

bruto = 2351
gastos = 456
neto = bruto - gastos
if neto > 0:
    print(f'Neto positivo {neto}')
else:
    print(f'Neto negativo {neto}')
    
# Ahora usanfdo el operador Walrus
bruto = 2351
gastos = 456
if(neto :=  bruto - gastos) > 0: #Simplificacion usando Walrus
    print(f'Neto positivo {neto}')
else:
    p 
    