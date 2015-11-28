# -*- coding: utf-8 -*-
__author__ = 'Richard'

####    EJEMPLO 1    ####
# Declaramos una lista con diferente tipos de datos
lista = [1, 3.1416, 'j', 'jarroba.com',  True]

print 'Imprimimos los elementos de una lista y el tipo de dato de cada elemento'
for l in lista:
    print '%s - %s' %(l, type(l))




####    EJEMPLO 2    ####

print '\n\n******    Ejemplo de los métodos para las listas    ******'

# Ejemplo de lista en la que guardaremos las demarcaciones en el fútbol
demarcaciones = list()


# Insertamos algunas demarcaciones
demarcaciones.append('Defensa')
demarcaciones.append('Lateral')
demarcaciones.append('MedioCentro')
demarcaciones.append('Centro Campista')
demarcaciones.append('Extremo')
print demarcaciones


# Vemos cuantos elementos tiene nuestra lista
numElem = len(demarcaciones)
print 'Número de elementos en la lista: %d' %numElem


# Insertamos elementos en posiciones determinadas
demarcaciones.insert(0, 'Portero')
demarcaciones.insert(6, 'Delantero')
print demarcaciones


# Concatenamos dos listas
lista2 = ['Arquero', 'Carrilero', 'Portero', 'Lateral']
demarcaciones.extend(lista2)
print demarcaciones


# Borramos la primera aparición del elemento 'Lateral' de la lista
demarcaciones.remove('Lateral')
print demarcaciones


# Borramos en tercer elemento de la lista PD: las lista empiezan en el elemento 0
demarcaciones.pop(2)
print demarcaciones


# Buscamos la posición del primer elemento con valor = 'Extremo'
print demarcaciones.index('Extremo')


# Vemos el número de veces que esta en la lista el elemento 'Portero' y 'Delantero'
print demarcaciones.count('Portero')
print demarcaciones.count('Delantero')


# Invertimos los elementos de las lista
demarcaciones.reverse()
print demarcaciones


# Hacemos una copia de la lista demarcaciones
copiaDemarcaciones = demarcaciones[:]
print 'Copia %s' %copiaDemarcaciones


# Borramos todos los elementos de la lista 'copiaDemarcaciones'
del copiaDemarcaciones[:]
print copiaDemarcaciones


# Ordenamos la lista demarcaciones por orden alfabético
demarcaciones.sort()
print demarcaciones

demarcaciones.sort(reverse=True)
print demarcaciones



####    EJEMPLO 3    ####
print '\n\n*******    Ordenación de listas    ******'
listaNumero = [5,2,9,1,12,6,8,3,4]

print 'Lista Desordenada'
print listaNumero

print 'Lista ordenada de forma ascendente (Aqui da igual pasarle "reverse=False" como parámetro)'
listaNumero.sort(reverse=False)
print listaNumero

print 'Lista ordenada de forma descendente'
listaNumero.sort(reverse=True)
print listaNumero