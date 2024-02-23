# A) Exercicios IF

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = int(input('Insira a quantidade desejada: '))
preco = int(input('Digite o preco: '))

if quantidade < 0 or preco < 0:
    print('Dados inválidos')
else:
    print('Dados válidos')

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

celcius = float(input('Digite o valor da temperatura em celcius: '))

if celcius > 26:
    categoria  = 'Alta'
elif celcius >= 18 and celcius <= 26:
    categoria = ('Normal')
else:
    categoria = ('Baixa')


print(f'A temperatura inputada: {celcius}° é categorizada como: {categoria}')

# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
else:
    print('Passou')


# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re

print('-'*40)
print('         Sistema de Verificação')
print('-'*40)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


while True:
    idade = int(input('Digita sua idade: '))
    if idade >= 18 and idade <= 65:
        print('Idade valida')
        break
    else:
        print('Dados invalidos - Idade valida entre 18 a 65 anos')

cond = True
while cond:
    email = input('Digite um e-mail valido: ') 
    if(re.fullmatch(regex, email)):
        print('E-mail valido')
        cond = False
    else:
        print("Dados invalidos - Digite um e-mail valido")

print('Dados validos - Cadastro realizado com sucesso!')

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
valor_limite = 10000

if transacao['valor'] > valor_limite or transacao['hora'] < 9 or transacao['hora'] > 18:
    print(f'TRANSAÇÃO SUSPEITA: A transação no valor de: {transacao['valor']} realizada as: {transacao["hora"]} hrs é suspeita pois foge aos padrões estabelecidos, caso não tenha realizado a transação entre em contato com o banco no numero 3333-4444')
else:
    print('Transação padrão')

# B) Exercicios FOR

# Exercicio 6. Contagem de Palavras em Textos
# Dado um texto, contar quantas vezes cada palavra única aparece nele.
    
texto = '"Na vastidão do universo, estrelas cintilam como jóias preciosas, refletindo a luz da criação. Criação que molda destinos e desperta paixões, paixões que alimentam o fogo da vida, vida que pulsa em cada batida do coração."'
    
palavras = texto.split(" ")

# Exercicio 7. Normalização de Dados
# Normalizar uma lista de números para que fiquem na escala de 0 a 1.
    
# Exercicio 8. Filtragem de Dados Faltantes
# Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
    
# Exercicio 9. Extração de Subconjuntos de Dados
# Dada uma lista de números, extrair apenas aqueles que são pares.
    
# Exercicio 10. Agregação de Dados por Categoria
# Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
    
