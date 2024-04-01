import numpy as np

# Vamos revisar funções adicionando type hints e Pydantic.

# Exercicio 1 - Calcular Média de Valores em uma Lista.

salarios = [1000, 2500, 3000, 5000, 1800]


def media(valores: int) -> int:
    media_salarial: float = sum(valores) / len(valores)
    return media_salarial


media_salarial = media(salarios)
print(media_salarial)

# Exercicio 2 - Filtrar Dados Acima de um Limite.

metricas = [10, 50, 45, 70, 80, 120, 15]
valores_acima_50 = []


def ver_valor(valores: list) -> list:
    for valor in valores:
        if valor > 50:
            valores_acima_50.append(valor)
    return valores_acima_50


print(ver_valor(metricas))


# Exercicio 3 - Contar Valores Únicos em uma Lista.

notas = [3, 5, 7, 7, 8, 9, 2]
valores_unicos = []


def ver_valor_unicos(valores: list) -> list:
    for valor in valores:
        if valor not in valores_unicos:
            valores_unicos.append(valor)
    return valores_unicos


print(ver_valor_unicos(notas))

# Exercicio 4 - Converter Celsius para Fahrenheit em uma Lista.

temperaturas_celcius = [32, 22, 25, 28, 35, 19]
temperaturas_fahrenheit = []


def celcius_fahrenheit(temperaturas: list, temperaturas_f: list) -> list:
    for temperatura in temperaturas:
        temperaturas_f.append(temperatura * 1.8 + 32)
    return temperaturas_f


celcius_fahrenheit(temperaturas_celcius, temperaturas_fahrenheit)
print(temperaturas_fahrenheit)

# Exercicio 5 - Calcular Desvio Padrão de uma Lista.

notas = [7, 8, 2, 9, 1]


def calc_desvio_padrao(valores: list) -> list:
    dp = np.std(valores)
    dp = f"{dp:.2f}"
    return dp


print(calc_desvio_padrao(notas))

# Na raça sem biblioteca
# import random

# notas = []
# for i in range(5):
#     notas.append(random.randint(1, 10))

# def media_valores(lista_valores: list) -> float:
#     media_numeros:float = sum(lista_valores) / len(lista_valores)
#     return media_numeros

# media_notas: float = media_valores(notas)

# lista_quadrado_diferenca = []
# def quadrado_diferenca(lista_valores: list) -> list:
#     for valor in lista_valores:
#         lista_quadrado_diferenca.append((valor - media_notas) ** 2)
#     return lista_quadrado_diferenca

# quadrado_diferenca_valores: list = quadrado_diferenca(notas)

# def variancia_conjunto(lista_valores: list):
#     variancia = sum(lista_valores) / len(lista_valores)
#     return variancia

# valor_variancia = variancia_conjunto(quadrado_diferenca_valores)

# def desvio_padrao(valor: float) -> float:
#     desvio_padrão = valor**0.5
#     return desvio_padrão

# dp: float = desvio_padrao(valor_variancia)
# print(f"O valor do Desvio Padrão da lista: {notas} é de {dp}")

# Exercicio 6 - Encontrar Valores Ausentes em uma Sequência.
