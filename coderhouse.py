estudiante = input ('Ingresar nombre del Estudiante :')
primer_nota = int (input ('Ingresar primer nota: '))
segunda_nota = int (input('Ingresar segunda nota: '))
tercer_nota = int (input ( 'Ingresar tercer nota: '))

print (f'El promedio ponderado de {estudiante} es :' ,primer_nota*15 /100 + segunda_nota*35/100 + tercer_nota *50/100)
print (f'El promedio normal de {estudiante} es :', primer_nota*1/2 + segunda_nota*1/2 + tercer_nota*1/2)
if primer_nota*15 /100 + segunda_nota*35/100 + tercer_nota *50/100 > 6 :
 print (f'El Estudiante {estudiante} aprobó :D')
else : 
    print (f'El Estudiante {estudiante} no aprobó D:')




