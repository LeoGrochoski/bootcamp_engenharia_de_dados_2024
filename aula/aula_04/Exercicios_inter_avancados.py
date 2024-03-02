# Exercicios de Lista

# Exercicios 6 - Eliminação de Duplicatas
# Dada uma lista de emails, remover todos os duplicados.

emails = ["joao@example.com", "paulo@example.com", "paulo@example.com", "rafael@example.com"]

print ("A lista é: " + str(emails)) # Convertendo para str para poder concatenar, listas não podem serem concatenadas

# Removendo duplicados
lista_sem_duplicados = list(set(emails)) 

# printing list after removal 
print ("A lista depois de remover os duplicados: " + str(lista_sem_duplicados)) 

# Exercicio 7 - Filtragem de Dados
# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

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


# Exercicio 8 - Ordenação Personalizada
# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

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

# Exercicio 9 - Agregação de Dados
# Dado um conjunto de números, calcular a média.

gastos_mes_janeiro = [100.0, 200.0, 75.0, 230.50, 24.33, 48.20]

media_gastos_janeiro = sum(gastos_mes_janeiro) / len(gastos_mes_janeiro)

print(media_gastos_janeiro)


# Exercico 10 - Divisão de Dados em Grupos
# Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
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
        

# Exercicios de Dicionario

# Exercicio 11. Atualização de Dados
# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico. 

# Exercicio 12. Fusão de Dicionários
# Dados dois dicionários, fundi-los em um único dicionário.

# Exercicio 13. Filtragem de Dados em Dicionário
# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# Exercicio 14. Extração de Chaves e Valores
# Dado um dicionário, criar listas separadas para suas chaves e valores.

# Exercicio 15. Contagem de Frequência de Itens
# Dada uma string, contar a frequência de cada caractere usando um dicionário.