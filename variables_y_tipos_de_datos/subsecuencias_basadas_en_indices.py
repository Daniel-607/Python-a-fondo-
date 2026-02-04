#Teniendo un objecto de t5ipo secuencia(sec), un numero entero que se utiliza como indice de la secuencia
#(ind),un numero entero para determinar el inicio de la secuencia(i_inicio),un entero para determinar el 
#final de la secuencia(i_fin)y un numero paso que determina el paso a sumar en cada iteracion hasta llegar
#a i_fin, se puede hacer las siguientes operaciones para obtener sub secuencvias de la secuencia sec

sec[ind]:#seleccion de un unico elemento, el de la posicion marcada por ind

sec[-ind]#seleccion de un unico elemento , el de la posicion ind comenzando a contar desde el fin de la secuencia
sec[i_inicio:i_fin]#selecion de subsecuencia desde la posicion i_inicio hasta i_fin
sec[i_inicio:]#selecion de subsecuencia desde la posicion i_inicio hasta el final de la secuencia con paso 1
sec[i_inicio: i_fin:paso]#selecion de subsecuencia desde la posicion i_inicio hasta la posicion i_fin
#se define un paso para ir sumando en cada iteracion hasta llegar a i_fin. El paso puede ser negativo
sec[:i_fin]:#Selecion de la secuencia hasta i_fin similar a sec[0:i9_fin]
sec[:i_fin:paso]:#selecion de la secuenciqa hastaq i_fin, pero con un paso que sera sumado enm cada iteracion hasta llegar a i_fin
sec[::paso]:#toda la secuenciaq pero utilizando el paso para recorrerlaq
sec[::]#copia la secuencia de forma superficial, similar a sec[::1]

#LOS pasos pueden ser negativos. En este caso, actuan de la misma forma p-ero recorriendo la secuencia en orden 
#inverso
a = [1, 2, 3, 4, 5]
a[2], a[4], a[-2]
#resultado (3,5,4)
a[3:20]
#(4,5)
a[1:5:2]
#(2,5)
a[::]
#(1,2,3,4,5)
a[::-1]
#(5,4,3,2,1)
