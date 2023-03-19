print ("*-CÁLCULO DE KW CONSUMIDO-*")
print (" ")

#----------VALORES INSERIDOS PELO USUÁRIO (POTÊNCIA, HORAS POR DIA E DIAS POR MÊS)
potencia = float(input("Informe a quantidade de WATT consumido por este equipamento: "))


horaDia = float(input("Informe a quantidade de horas diárias gastas neste equipamento: "))


diaMes = int(input("Informe quantos dias esse equipamento é utilizado: "))
#----------------------------------------------------------------------------------

#CÁLCULO kWh
kWh = (potencia * horaDia * diaMes) / 1000
#---------------------------------------------

#VALOR MÍNIMO
if kWh == 0:
    
    valor = 11.90

# UNIDADE DE KWH = R$0,20
elif kWh < 150:

    valor = kWh * 0.2

## UNIDADE DE KWH = R$0,25
elif kWh < 500:

    valor = kWh * 0.25

# UNIDADE DE KWH = R$0,30
else:
    
    valor = kWh * 0.30



print("O valor gasto neste equipamento de acordo com o kWh é de R$:", valor)


