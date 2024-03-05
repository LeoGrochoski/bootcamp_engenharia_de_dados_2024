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
    for i in range(2,numero):
        if (numero%i) == 0:
            return False
        return True

numero_primo = verificador_primo(valor)

if numero_primo == True:
    print(f"O numero: {valor} é primo")
else:
    print(f"O numero: {valor} não é primo")

# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas