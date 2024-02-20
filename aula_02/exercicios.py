# Exercícios Aula 2

# Inteiros (int)

print(40*'-')
print('      Exericicios do Tipo Inteiro          ')
print(40*'-')

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

print('Exercicio 1 - Soma de valores')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 + num2
print(f'O resultado da soma é:, {resultado}')

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

print('Exercicio 2 - Calculo de resto de divisão')
num_user = int(input('Digite um número: '))

resultado = num_user % 5
print(f'O resto da divisão do numero {num_user} dividido por 5 é: ', resultado)

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print('Exercicio 3 - Multiplicação de valores')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 * num2
print(f'O valor de {num1} multiplicado por {num2} é: ', resultado)

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print('Exercicio 4 - resultado da divisao inteira')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resultado = num1 // num2
print(f'O resultado da divisao inteira do número {num1} pelo {num2} é: ', resultado)

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print('Exercicio 5 - Valor ao quadrado')
num1 = int(input('Digite um número inteiro: '))

resultado = num1 * num1
print(f'{num1} ao quadrado é: ', resultado)

# Números de Ponto Flutuante (float)

print(40*'-')
print('      Exericicios do Tipo Float          ')
print(40*'-')

# 1 - Escreva um programa que receba dois números flutuantes e realize sua adição.

print('Exercicio 1 - Adição de números decimais')
num1 = float(input('Digite o primeiro número com decimal: '))
num2 = float(input('Digite o segundo número com decimal: '))

resultado = num1 + num2
print(f'O resultado da soma dos números: {num1} e {num2} é: ', resultado)

# 2 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

print('exercicio 2 - Média de números decimais')
num1 = float(input('Digite o primeiro número com decimal: '))
num2 = float(input('Digite o segundo número com decimal: '))

media = (num1 + num2) / 2
print(f'A media dos números: {num1} e {num2} é: ', media)

# 3 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print('Exercicio 3 - Potenciação')
base = float(input('Digite o valor da base: '))
exp = float(input('Digite o valor do expoente: '))

result = base ** exp
print(f'O resultado da Eponenciação de {base} por {exp} é: ', result)

# 4 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

print('Exercicio 4 - Conversão de temperatura de Celcius para Fahrenheit')
celcius = float(input('Digite o valor da temperatura em celcius: '))
fahrenheit = celcius * 1.8 + 32
print(f'A temperatura de {celcius}° Celcius, é de {fahrenheit:.2f}° Fahrenheit')

# 5 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

print('Exercicio 5 - Calculo de área de círculo')
raio = float(input('Digite o raio do circulo '))
area = 3.142 * (raio * raio)
print(f'A area o circulo é: {area:.2f}')

#Strings (str)

print(40*'-')
print('      Exericicios do Tipo Str          ')
print(40*'-')

# 1 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

print('Exercicio 1 - Exibindo input em letras maisculas')
nome_usuario = input('Digite seu usuario valido: ')
print(f'Seja bem vindo, {nome_usuario.upper()}')

# 2 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

print('Exercicio 2 - Exibindo input em letras minusculas')
nome_completo = input('Digite seu nome completo: ')
print(f'Muito prazer, {nome_completo.lower()}')

# 3 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

print('Exercicio 3 - Retirada de espaços em branco')
frase = input('Insira uma frase: ')
print(frase.strip)

# 4 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

print('Exercicio 4 - separando os dados do input de data, por dia, mes e ano')
data = input('insira uma data no formado dd/mm/yyyy: ')
data.split("/")
print(data)

# 5 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

print('Exercicio 5 - Concatenação de strings')
frase1 = input('Digite o nome de uma fruta: ')
frase2 = input('Digite o nome de uma cor: ')
chave = frase1 + frase2
print(f"A chave de segurança é: {chave}")

# Booleanos (bool)

print(40*'-')
print('      Exericicios do Tipo Bool          ')
print(40*'-')


# 1 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.


# 2 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.


# 3 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.


# 4 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.


# 5 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.