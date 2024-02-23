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
