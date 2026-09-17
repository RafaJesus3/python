idade = int(input("Digite sua idade: "))
cnh = input("Digite se você tem CNH (sim ou nao): ").lower()

if idade<0:
    print("Idade Invalida")
elif idade>=18 and cnh =="sim":
    print("Permitido a dirigir")
elif idade>=18 and cnh=="nao":
    print("Tem idade para tirar CNH, mas não pode dirigir")
elif idade<18 and cnh=="nao":
    print("Não é permitido a dirigir")
elif idade<18 and cnh=="sim":
    print("Você não tem idade suficiente para ter uma CNH definitiva")
else:
    print("Valores invalidos")