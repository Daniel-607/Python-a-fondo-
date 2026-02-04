cadena = input ("Por favor ingrese una cadena ")
candena = cadena.lower()

l_cadena = list(cadena)

l_cadena_alReves = list(cadena)
l_cadena_alReves.reverse()

while " " in l_cadena:
    l_cadena.remove(" ")

while " " in l_cadena_alReves:
   l_cadena_alReves.remove(" ")
   
if l_cadena == l_cadena_alReves:
       print("La cadena intrudcida es un palindromo")
else:
    print("La cadena intrudcida No es un palindromo")
   
