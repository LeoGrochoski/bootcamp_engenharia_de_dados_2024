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
