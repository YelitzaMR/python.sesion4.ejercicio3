#Informamos lo que hará el programa
print('Ahora mostraremos los números del 100 al 1')
#llenamos una lista con los números
listaNumeros: [int]=[]
for i in range (1,101):
    listaNumeros.append(i)
#usamos la función reversed para cambiar orden de la lista que llenamos antes
listaInvertida=list(reversed(listaNumeros))
print(listaInvertida)




