# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
# Formula do bonus: 1000 + salario * bonus

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salario: "))
bonus_perc = float(input("Digite a porcentagem do seu bonus recebido: "))

bonus_perc = bonus_perc / 100

bonus_fixo = 1000
bonus = bonus_fixo + salario * bonus_perc

print(f'Ola {nome}, seja muito bem vindo ao Portal Finanças')
print(f'Seu salario é de: {salario}')
print(f'Seu bonus foi de: R${bonus}')