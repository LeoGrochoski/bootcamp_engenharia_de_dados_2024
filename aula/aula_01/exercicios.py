# Exercicios Aula 01

# 1 - Crie programa que o usuário digita o seu nome e retorna o número de caracteres.

print('Exercício 1')

nome_usuario = input('Digite seu nome: ')
print(f'O quantidade de caracteres do seu nome é: ', len(nome_usuario))

# 2 = Criar um programa onde o usuário digite dois valores e apareça a soma

print('Exercício 2')

valor1 = int(input('Digite um primeiro valor numerico: '))
valor2 = int(input('Digite um segundo valor numerico: '))

print(valor1 + valor2)

# Exercicio de teste

nome = input("Digite seu nome: ")
salario = int(input("Digite o valor do seu salario: "))
bonus = int(input("Digite o valor do seu bonus recebido: "))

if salario > bonus:
    proporcao = 'Menor que'
elif salario < bonus:
    proporcao = 'Maior que'
else:
    proporcao = 'Igual a'


print(f'Ola {nome}, seja muito bem vindo ao Portal Finanças')
print(f'Seu salario é de: {salario}')
print(f'Seu bonus foi de: R${bonus} e ele foi: {proporcao} seu salario')