idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (sim ou não): ")

if idade>=18 and cnh == "sim":
    print("Você é permitido a dirigir")
elif idade>=18 and cnh == "nao":
    print("Você tem o direto em solicitar o CNH, mas não pode dirigir sem a CNH")
else:
    print("Você não tem idade para dirigir ")


# Outro jeito de fazer

if idade>=18:
    if cnh=="sim":
        print("Você é permitido a dirigir")
    else:
        print("Você tem o direto em solicitar o CNH, mas não pode dirigir sem a CNH")
else:
    print("Você não tem idade para dirigir ")