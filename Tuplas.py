###--------------Tuplas---------------###

tup=(1,2,3,4,5,6,7,8)

# recorrer una tupla 

for tupla in tup:
    print(tupla)


# agregamos un elemnto a la tupla 

tupla1 = (1, ['a', 'b'])
tupla1[1].append('c')  # tupla[1] hace referencia a la lista
print(tupla1)


# Cómo saber si un elemento está en una tupla 


colores = 'azul', 'blanco', 'negro'
if 'azul' in colores:
    print('Sí')


if 'verde' not in colores:
    print('No')
     
