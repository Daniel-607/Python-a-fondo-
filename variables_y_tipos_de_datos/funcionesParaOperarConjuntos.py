>>> setA, setB = {3.14, 4j, 'hola'}, {'Juan', 'hola'}
>>> setA | setB #igual que setA.union(setB) esta une dos conjuntos
{3.14, 'Juan', 'hola', 4j}
>>> setA & setB #Igual que setA.intersection(setB) crea un nuevo conjunto solo con los elementos en comun 
{'hola'}
>>> setA - setB #Igual que setA.difference(setB) crea un nuevo conjunto con los elementos de de setA que no estan en setB
{3.14, 4j}
>>> setA ^ setB #Es lo mismo que decir que setA.symetric_difference(setB) crea un nuevo conjunto con los elementos que esten en setA y setB Pero no en ambos
{3.14, 4j, 'Juan'}
>>> setB.copy() #Crea una copia de setB
{'hola', 'Juan'}