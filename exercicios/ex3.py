horas = int(input("Digite seu número: "))
minutos = int(input("Digite seu número: "))

if ((horas <= 23 and horas >= 0) and (minutos < 59 and minutos > 0)):
    print(f"Seu hórario é {horas:02d}:{minutos:02d}")
else:
    print("Horas ou minutos invalidos.")

