# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Listas
notas = [7.9, 9.7, 8.2]

#Criando Listas
lista = []
lista = list()
lista = [28, 'Mirelle', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

# Indexação: Acessando um elemento por meio de índice
lista = [10, 'Mirelle', 3.14159, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#Slice

lista = [10, 50, 30, 40, 25, 60, 5]

# Índice 0 até menor que 3
print(lista[0:3])
print(lista[3:6])
print(lista[3:]) # vai até o final da lista
print(lista[2:6:2]) # step 2

# Iteração com FOR

#1. Utilizando os próprios elementos da lista

# percorrer cada elemento da lista
for elemento in lista:
    print(elemento)

#2. Utilizando os índices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])
    
# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# Append

print('Antes do append: ', lista)
lista.append(3)
print('Depois do append: ', lista)

# Insert

lista.insert(2,10)
print('Depois do insert: ', lista)

# Extend

lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend: ', lista)

# Pop

lista.pop()
print('Lista apos o pop: ', lista)

# Remove

lista.remove(3)
print('Depois do remove: ', lista)

# Count

print('Quantidade de 2 na lista: ', lista.count(2))

# Index

print('Índice do elemento 12: ', lista.index(12))

# Sort

lista.sort()
#lista.sort(reverse=True)-> Ordem decrescente
print(lista)

# FUNÇÕES PARA LISTAS

# Len

print(len(lista))

# Sum

print(sum(lista))

# Max

print('Maior elemento da lista: ', max(lista))

# Min

print('Menor elemento da lista: ', min(lista))