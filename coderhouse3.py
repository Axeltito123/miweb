""" Python - Clase 03

Este archivo contiene líneas de código que no están
pensadas como un programa, sino como referencia.

"""

# El Tipo "lógico" (AKA bool)

1 == 2
mi_variable_booleana = 1 == 2
mi_otra_variable_booleana = (1 == 1)
mi_tercer_variable_booleana = True
type(mi_variable_booleana)


# Operadores relacionales
0 > 1
1 < 10
1 >= 4/3
type(5)==str,
type("5")==int
expresiones_booleanas = [
    False == True,
    10 >= 2*4,
    33/3 == 11,
    True > False,
    True*5 == 2.5*2
]

# Operadores lógicos
mi_variable = not True
mi_variable = not 1 == 1
mi_variable = True and False
mi_variable = 1 == 1 and 2 == 2
mi_variable = 1 == 1 or 2 == 2
mi_variable = 1 == 2 and 4 == 5
mi_variable = 1 == 2 or "mariano" == "mariano"
mi_variable = 1 == 2 or "mariano" == "Mariano".lower()
mi_variable = not "mariano" == "Mariano" # !

#print (mi_variable)
expresiones = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]

#print (expresiones)


nombre = input ('')
edad =  int (input (''))

mi_variable_booleana2 = (nombre != "****") and (edad > 10  and edad < 18 ) and (len(nombre)>10) and (edad*4 > 40 )
print (mi_variable_booleana2)