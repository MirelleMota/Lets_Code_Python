# Para i dentro de uma faixa de x a y, faça tal coisa:

'''for variavel in range(10):
    print(variavel)

for variavel2 in range(1,10):
    print(variavel2)
    
for variavel3 in range(1,12,3):
    print(variavel3)'''

#com a formatação de string (f), condigo injetar dentro da string.

soma = 0

for i in range(1,4):
    nota = float(input(f'Informe a sua nota {i}: '))
    
    soma = soma + nota
    
print(soma /3)