
print ("*-VERIFICAÇÃO DE DIVISÃO EXATA-*")

#NÚMEROS INSERIDOS PELO USUÁRIO
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

#RESTO 0
if num1%num2 == 0:
    print ("A divisão é exata")

#DIVISÃO QUEBRADA
else:
    print ("A divisão não é exata")

