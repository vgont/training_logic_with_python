
#NÚMERO DIGITADO PELO USUÁRIO
num = float(input("Digite um número e, caso seja maior que 100, irei adicionar +150 a esse número: "))


#SE NÚMERO > 100 ADICIONE +150 E EXIBA O NÚMERO JÁ SOMADO
if num > 100:
    num += 150
    print ("O número digitado é maior do que 100! Seu número atual então é:", num)

 #SE NÚMERO <= 100 APENAS EXIBE O NÚMERO
else:
    print ("Seu número é:", num) 