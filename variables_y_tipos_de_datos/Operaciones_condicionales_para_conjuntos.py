setA, setB = {1,2,3}, {1,2,3,4} # se declaran dos conjuntos tipo set 
>>> 4 in setA, 4 in setB, len(setA) #Aqui se pregunta si 4 esta en el conjunto setA y en el conjunto setB y  su ves atraves de len se solicit el valor o la cantidad de datos de setA 
(False, True, 3)
>>> setA.isdisjoint(setB), setA.isdisjoint({4,5}) #Se pregunta si no existen elementos en comun entrer setA y setB  lo cual es cierto por eso devuelve false el siguiente es lo contrario por eso devuel;ve true
(False, True)
>>> setA.issubset(setB), setA.issuperset(setB) #se solicita que devuelva verdadero o falso si los elementos de serB estan en setA
(True, False)