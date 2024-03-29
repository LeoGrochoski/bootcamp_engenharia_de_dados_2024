
# Exercícios TypeError, Type Check e Type Conversion em Python

# Aqui estão cinco exercícios que envolvem `TypeError`, verificação de tipo (`type check`), 
# o uso de `try-except` para tratamento de exceções e a utilização da estrutura condicional `if`. 
# Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando `try-except`, 
# garantir que a entrada seja numérica, tratando qualquer `ValueError`. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

print('Exercício 21: Conversor de Temperatura')

try:
    celcius = float(input('Digite o valor da temperatura em celcius: '))
    fahrenheit = celcius * 1.8 + 32
    print(f'A temperatura de {celcius}° Celcius, é de {fahrenheit:.2f}° Fahrenheit')
except ValueError:
    print('Digite um valor valido para temperatura em celcius')

# Exercício 22: Verificador de Palíndromo

# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize `try-except` para garantir que a entrada seja uma string. 
# Dica: Utilize a função `isinstance()` para verificar o tipo da entrada.

print('Exercício 22: Verificador de Palíndromo')

try:
    entrada = input('Digite uma palavra ou uma frase para verificar se é um palindromo: ')
    if isinstance(entrada, str):
        entrada_ajustada = entrada.replace(' ', '').lower()
        if entrada_ajustada == entrada_ajustada[::-1]:
            print(f'A palavra/frase {entrada} é um palíndromo')
        else:
            print(f'A palavra/frase {entrada} não é um palíndromo')
except:
    print('Insira uma palavra ou frase valida')


# Exercício 23: Calculadora Simples

# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use `try-except` para lidar com divisões por zero e entradas não numéricas. 
# Utilize `if-elif-else` para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

print('Exercício 23: Calculadora Simples')

try:
    print('--------------------------------------------------------------------')
    print('                          CALCULADORA                               ')
    print('--------------------------------------------------------------------')
    num1 = float(input('Insira o primeiro valor: '))
    num2 = float(input('Insira o segundo valor: '))
    operador = input('Digite o sinal da operação que deseja: ')
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    elif operador == '*':
        resultado = num1 * num2
    else:
        print('Operador invalido')
    print(resultado)
except ValueError:
    print('Erro: Entrada inválida. Certifique-se de inserir números.')

# Exercício 24: Classificador de Números

# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", 
# "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

print('Exercício 24: Classificador de Números')

try:
    valor = int(input('Digite um numero: '))
    if valor > 0:
        print(f'O número {valor} é positivo')
    elif valor < 0:
        print(f'O número {valor} é negativo')
    else:
        print(f'O número {valor} é zero')
    if valor % 2 == 0:
        print(f'O número {valor} é par')
    else: 
        print(f'O número {valor} é impar')
except ValueError:
    print('Certifique-se de fornecer um valor valido')

# Exercício 25: Conversão de Tipo com Validação
 
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

print('Exericio 25 - Conversão de Tipo com Validação')

lista_numerica = input('Digite uma lista de numeros separados por virgula: ')
numeros_str = lista_numerica.split(",")
lista_int = []

try:
    for num in numeros_str:
        lista_int.append(int(num.strip()))
    print('Lista tratada', lista_int)
except:
    print('Digite numeros inteiros validos')

todos_inteiros = all(isinstance(num, int) for num in lista_int)

if todos_inteiros:
    print('Todos os números na lista são inteiros.')
else:
    print('Pelo menos um dos números na lista não é um inteiro.')
