print ("Cada produto custa R$20,00")

#DETERMINANDO PRODUTO
produto = 20.00

#NÚMERO INSERIDO PELO USUÁRIO (QUANTIDADE)
quantidade = int(input("Insira a quantidade de produtos que você desejar: "))

#CÁLCULO DO *TOTAL*
total = produto*quantidade

#DETERMINA CADA DESCONTO E JÁ FAZ A CONTA DIRETO
desc1 = total * 0.9
desc2 = total * 0.8
desc3 = total * 0.7
desc4 = total * 0.6

#SEM DESCONTO
if total < 100:
    print ("O total da sua compra é: R$", total)

#10% DESCONTO
elif total<=199:
    print("Você recebeu um desconto de 10%! O total da sua compra é: R$", desc1)

#20% DESCONTO
elif total <= 299:
    print("Você recebeu um desconto de 20%! O total da sua compra é: R$", desc2)

#30% DESCONTO
elif total <= 400:
    print("Você recebeu um desconto de 30%! O total da sua compra é: R$", desc3)

#40% DESCONTO
else:
    print("Você recebeu um desconto de 40%! O total da sua compra é: R$", desc4)
