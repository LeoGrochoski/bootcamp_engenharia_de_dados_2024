# Exercícios de Funções

# Exercicio 16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

lista_numeros = [10, 20, 30, 40, 50]

def soma(valor: list) -> int:
    return sum(valor)

numeros_somados = soma(lista_numeros)
print(numeros_somados)

# Exercicio 17 - Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

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

# Exercicio 18 - Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.



# Exercicio 19 - Implemente uma função que receba dois argumentos: uma lista de números e um número.
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

lista_num: list = [1, 7, 4, 3]
valor: int = 8
nv_lista: list = []

def soma_lista(lst: list, num: int) -> list:
    for l in lst:
        nl: int = l + num
        nv_lista.append(nl)
    return nv_lista

def forma_pares(lst: list) -> list:
    if len(lst) <= 1:
        return []
    
    pares: list = [(lst[0], x) for x in lst[1:]]
    
    return pares + forma_pares(lst[1:])

resultado1: list = soma_lista(lista_num, valor)
print(resultado1)

resultado2: list = forma_pares(nv_lista)
print(resultado2)

# Exercicio 20 - Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

alunos: dict = {"aluno_01":"Leonardo", "aluno_02":"Jose", "aluno_03":"Paulo", "aluno_04":"Kleber", "aluno_05":"Felipe"}
ordem_alunos: list = [] 

# def ordenador(dicionario: dict):
    
    
    
    
for i in alunos:
    print(i)