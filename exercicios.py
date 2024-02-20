# Exercícios Aula 2

# Inteiros (int)

print(40*'-')
print('      Exericicios do Tipo Inteiro          ')
print(40*'-')

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

print('exercicio 1 - Soma de valores')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 / num2
print(f'O resultado da soma é:, {resultado:.2f}')

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

print('exercicio 2 - Calculo de resto de divisão')
num_user = int(input('Digite um número: '))

resultado = num_user % 5
print(f'O resultado do resto da divisão por 5 do número digitado pelo usuario é: ', resultado)

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print('exercicio 3 - Multiplicação de valores')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 * num2
print(f'O resultado do número {num1} multiplicado por {num2} é: ', resultado)

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print('exercicio 4 - resultado da divisao inteira')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 // num2
print(f'O resultado da divisao inteira do número {num1} pelo {num2} é: ', resultado)

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print('exercicio 5 - Valor ao quadrado')
num1 = int(input('Digite um número inteiro: '))

resultado = num1 ** num1
print(f'O quadrado do numero {num1} é: ', resultado)

# Números de Ponto Flutuante (float)

print(40*'-')
print('      Exericicios do Tipo Float          ')
print(40*'-')

# 1 - Escreva um programa que receba dois números flutuantes e realize sua adição.

print('exercicio 1 - Adição de números decimais')
num1 = int(input('Digite o primeiro número com decimal: '))
num2 = int(input('Digite o segundo número com decimal: '))

resultado = num1 + num2
print(f'O resultado da soma dos números: {num1} e {num2} é: ', resultado)

# 2 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

print('exercicio 2 - Média de números decimais')
num1 = int(input('Digite o primeiro número com decimal: '))
num2 = int(input('Digite o segundo número com decimal: '))

media = (num1 + num2) / 2
print(f'A media dos números: {num1} e {num2} é: ', media)

# 3 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print('exercicio 3 - Potenciação')
num1 = int(input('Digite o valor da base: '))
num2 = int(input('Digite o valor do expoente: '))

media = (num1 + num2) / 2
print(f'A media dos números: {num1} e {num2} é: ', media)

# 4 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.


# 5 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.



#Strings (str)

print(40*'-')
print('      Exericicios do Tipo Str          ')
print(40*'-')


# 1 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 2 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 3 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 4 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 5 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

# Booleanos (bool)

print(40*'-')
print('      Exericicios do Tipo Str          ')
print(40*'-')


# 1 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 2 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 3 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 4 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 5 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.