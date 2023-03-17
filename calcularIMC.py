print ("*-CÁLCULO DE IMC-*")

# Informações inseridas pelo usuário
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))


#conta da Massa
massaCorp = peso / (altura**2)

if massaCorp < 26:
    print ("Grau de Obesidade: Normal")

elif massaCorp >= 26 and massaCorp < 30:
    print ("Grau de Obesidade: Obeso")

else:
    print ("Grau de Obesidade: Obeso Mórbido")