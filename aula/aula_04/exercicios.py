# Exercicio 1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_quadrado = []

for i in numero:
    numero_quadrado.append(i ** 2)

print(f'Lista de numeros: ', numero)
print(f'Lista de numeros ao quadrado: ', numero_quadrado)
    

# Exercicio 2 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens = ["Python", "Java", "C++", "JavaScript"]

print(linguagens)

linguagens.remove('C++')
linguagens.append('Ruby')

print(linguagens)

# Exercicio 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

livro = {
    "titulo":"Ensaio Sobre a Cegueira",
    "autor":"Jose Saramago",
    "ano publicacao":"1995"
}

print(livro["titulo"])
print(livro["autor"])
print(livro["ano publicacao"])


# Exercicio 4 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

valor = "tijolo"
letras = [l for l in valor]
print(letras)
armazem = {}

for letra in letras:
    if letra in armazem:
        armazem[letra] += 1
    else:
        armazem[letra] = 1

print(armazem)

# Exercicio 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

lista_frutas = ["maçã", "banana", "cereja"]
frutas = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

somador = 0
valor_compras = []

for i in range(len(lista_frutas)):
    fruta = (lista_frutas[somador])
    valor = (frutas[fruta])
    print(f'O valor da fruta: {fruta} é de: {valor}')
    valor_compras.append(valor)
    somador += 1
print(f'O valor total das compas é de: R$ {sum(valor_compras)}')
