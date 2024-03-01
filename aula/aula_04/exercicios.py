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

from collections import Counter

palavra = "tijolo".split()

armazem = []

c=Counter()
for p in palavra:
    c.update(set(p))
print(c.most_common())
print([a[0] for a in c.most_common()])

# Exercicio 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.