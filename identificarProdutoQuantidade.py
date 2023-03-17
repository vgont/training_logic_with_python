print ("Cada produto custa R$20,00")

produto = 20.00
quantidade = int(input("Insira a quantidade de produtos que você desejar: "))

total = produto*quantidade

desc1 = total * 0.9
desc2 = total * 0.8
desc3 = total * 0.7
desc4 = total * 0.6

if total < 100:
    print ("O total da sua compra é: R$", total)

elif total<=199:
    print("Você recebeu um desconto de 10%! O total da sua compra é: R$", desc1)

elif total <= 299:
    print("Você recebeu um desconto de 20%! O total da sua compra é: R$", desc2)

elif total <= 400:
    print("Você recebeu um desconto de 30%! O total da sua compra é: R$", desc3)

else:
    print("Você recebeu um desconto de 40%! O total da sua compra é: R$", desc4)
