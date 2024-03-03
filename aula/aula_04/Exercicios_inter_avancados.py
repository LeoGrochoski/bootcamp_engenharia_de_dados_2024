# # Exercicios de Lista

# # Exercicios 6 - Eliminação de Duplicatas
# # Dada uma lista de emails, remover todos os duplicados.
print('Exercicio 6 - Eliminação de Duplicatas')

emails = ["joao@example.com", "paulo@example.com", "paulo@example.com", "rafael@example.com"]

print ("A lista é: " + str(emails)) # Convertendo para str para poder concatenar, listas não podem serem concatenadas

lista_sem_duplicados = list(set(emails)) 

print ("A lista depois de remover os duplicados: " + str(lista_sem_duplicados)) 

# # Exercicio 7 - Filtragem de Dados
# # Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

print('Exercicio 7 - Filtragem de Dados')

idades = [8, 18, 28, 15, 29, 49, 37, 50, 11]

maiores_18 = []
menores_18 = []

for idade in idades:
    if idade >= 18:
        maiores_18.append(idade)
    else:
        menores_18.append(idade)

print(f"Essas idades são maiores ou iguais a 18 anos: {maiores_18}")
print(f"Essas idades são menores que 18 anos: {menores_18}")

# # Exercicio 8 - Ordenação Personalizada
# # Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

print('Exercicio 8 - Ordenação Personalizada')

lista_dicionarios = [{"nome":"paulo", 
                      "idade":28, 
                      "email":"paulo@gmail.com"}, 
                      {"nome":"nicolas",
                       "idade":10,
                       "email":"nico@oulook.com"}, 
                       {"nome":"jose",
                        "idade":40,
                        "email":"zerodri1984@yahoo.com"}]

nome_ordenados = []

for dicionario in lista_dicionarios:
    nome_ordenados.append((dicionario["nome"]))

print(sorted(nome_ordenados))

# # Exercicio 9 - Agregação de Dados
# # Dado um conjunto de números, calcular a média.

print('Exercicio 9 - Agregação de Dados')

gastos_mes_janeiro = [100.0, 200.0, 75.0, 230.50, 24.33, 48.20]

media_gastos_janeiro = sum(gastos_mes_janeiro) / len(gastos_mes_janeiro)

print(media_gastos_janeiro)

# # Exercico 10 - Divisão de Dados em Grupos
# # Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

print('Exercicio 10 - Divisão de Dados em Grupos')

import random

lista_valores = []

for i in range(5):
    valores = random.randint(1, 11)
    lista_valores.append(valores) 

valores_pares = []
valores_impares = []

for valor in lista_valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print(valores_pares)
print(valores_impares)
        
# # Exercicios de Dicionario

# # Exercicio 11. Atualização de Dados
# # Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico. 

print('Exercicio 11 - Atualização de Dados')

produtos = [{"nome":"Martelo de Unha 20mm Tramontina", "valor":29.00},
            {"nome":"Broca para Concreto 6x100mm", "valor":11.49},
            {"nome":"Lixa para Madeira e Massa Grão 80 ", "valor":3.20},
            {"nome":"Tinta Impermeabilizante Emborrachada Branca Fosca 18L", "valor":474.90}]

for produto in produtos:
    for item in produto:
        if produto.get(item) == 29.00:
            produto.update({item: 31.00})

print(produtos[0])

# # Exercicio 12. Fusão de Dicionários
# # Dados dois dicionários, fundi-los em um único dicionário.

print('Exercicio 12 - Fusão de Dicionários')

clientes_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
clientes_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }
clientes_1.update(clientes_2)
print('Atualizando Dicionario:')
print(clientes_1)

# # Exercicio 13 - Filtragem de Dados em Dicionário
# # Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

print('Exercicio 13 - Filtragem de Dados em Dicionário')

catalogo = {"calça":50,  
           "camiseta":200, 
           "tenis":34,
           "jaqueta":15, 
           "sueter":0, 
           "meia":10,
           "cachicol":0, 
           }

print(catalogo)

a = (catalogo.items())

itens_em_estoque = []

for item in a:
    if item[1] > 0:
        itens_em_estoque.append((item[0]))

print(f"Os itens disponiveis em estoque são: {itens_em_estoque}")

# Exercicio 14. Extração de Chaves e Valores
# Dado um dicionário, criar listas separadas para suas chaves e valores.

print('Exercicio 14 - Extração de Chaves e Valores')

catalogo = {"calça":50,  
           "camiseta":200, 
           "tenis":34,
           "jaqueta":15, 
           "sueter":0, 
           "meia":10,
           "cachicol":0, 
           }

itens = []
quantidades = []

a = (catalogo.items())

for item in a:
    itens.append((item[0]))
    quantidades.append((item[1]))

print(itens)
print(quantidades)

# Exercicio 15. Contagem de Frequência de Itens
# Dada uma string, contar a frequência de cada caractere usando um dicionário.

print('Exercicio 15 - Contagem de Frequência de Itens')

palavra = "verdade"

contagem_letras = {}

for letra in palavra:
    if letra in contagem_letras:
        contagem_letras[letra] += 1
    else:
        contagem_letras[letra] = 1

print(contagem_letras)