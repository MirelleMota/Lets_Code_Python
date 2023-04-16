# DICIONÁRIOS

# Criando Dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Mirelle', 'idade': 28, 'altura': 1.56 }

print(dicionario['idade'])

# Adicionando elemementos em um dicionário

dicionario['programadora'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])
    
# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)



# Adicionando elementos em um dicionário