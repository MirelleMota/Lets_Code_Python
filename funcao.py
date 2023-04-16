# FUNÇÕES

# print() - Imprime uma mensagem
# input() - Retorna um dado informado pelo usuário (entrada padrão)
# len() - Recebe uam lista e retorna o tamanho da mesma
# max() - Retorna o maior valor de uma lista

# 2. Criação de Funções

# Função Inicial

def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você aqui conosco!')

saudacao()

# Função com parâmetros

def saudacao(nome,curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Mirelle', 'Python')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Mirelle')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10,20)
#resultado = calculadora(10,20, '-')

print(resultado)