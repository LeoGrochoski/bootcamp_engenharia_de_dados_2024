# Exercícios de Funções

#Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

lista_numeros = [10, 20, 30, 40, 50]

def soma(valor: list) -> int:
    return sum(valor)

numeros_somados = soma(lista_numeros)
print(numeros_somados)

#Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

valor = int(input("Digite um valor para verificação se é primo: "))

def verificador_primo(numero: int) -> int:
    if numero > 1 and numero / 1 == numero and numero % numero == 0:
        print("Numero Primo")
    else:
        print("Não é um numero primo")
    
numero_primo = verificador_primo(valor)

#Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

#Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

#Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas