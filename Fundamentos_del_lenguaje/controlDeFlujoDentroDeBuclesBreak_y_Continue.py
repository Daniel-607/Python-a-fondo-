i=0
while i < 50:
    print(i)
    i += 1
    if i >3:
        break

for i, name in enumerate(['pepe', 'maria', 'juan', 'mario', 'paloma']):#enumerate lo que hace es que devuelve el indice y el valor de la lista y atraves del in cada uno lo asigna a una varieble correspondiente 
    print(f'{i}: {name}')
    if i > 1:
        break
    
for name in ['pepe', 'paloma', 'Maria', 'Manuel', 'Emilio', 'Jose', 'Antonia']:
    if len(name) < 5:# si lan longitud de la variable name es menor a 5 entonces continue
        continue #Omite la ejecucion cuando name tiene menos de 5 caracteres 
    print(name)
    