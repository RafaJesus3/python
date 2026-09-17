idade = int(input("Digite sua idade: "))
cnh = input("Digite se você tem CNH (sim ou nao): ").lower()

# x é o valor que vem da variavel idade
# foi definido uma variavel genérica para informar um valor possível (no caso o X)
#x é a idade
#y e a cnh

match idade, cnh:
    case i,c if i >=18 and c=="sim":
        print("Permitido a dirigir")
    case i,c if i <18 and c=="nao":
        print("Não é permitido a dirigir")
    case i,c if i >=18 and c=="nao":
        print("Você tem a idade para solicitar o CNH, mas não pode dirigir.")
    case i,c if i <18 and c=="sim":
        print("Voce é menor idade, porque voce tem CNH?")
    case _:
        print("Valores inválidos")


# OU

match idade, cnh:
    case i, _ if i < 0:
        print()
    case i, "sim" if i >=18 :
        print("Permitido a dirigir")
    case i, "nao" if i <18 :
        print("Não é permitido a dirigir")
    case i, "nao" if i >=18 :
        print("Você tem a idade para solicitar o CNH, mas não pode dirigir.")
    case i, "sim" if i <18 :
        print("Voce é menor idade, porque voce tem CNH?")
    case _:
        print("Valores inválidos")