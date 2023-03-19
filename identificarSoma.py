#NÚMEROS INSERIDOS PELO USUÁRIO
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

#CÁLCULO SOMA
soma = num1 + num2

# NÚMERO > 0
if soma > 0:
    print("Maior que zero")

# NÚMERO = 0
elif soma == 0:
    print("Igual a zero")

#NÚMERO < 0
else:
    print("Menor que zero")