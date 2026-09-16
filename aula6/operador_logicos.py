#Operadores lógicos

# > Maior que
# < Menor que
# >= Maior ou igual
# <= Menor ou igual
# == igualdade
# != Diferença


#and

usuario = str(input("Digite seu usuario: "))
senha = input("Digite a senha: ")

if senha != "fiap" or usuario != "admin":
    print("Senha ou usuario incorretos")
else:
    print("Acesso permitido!")


if senha == "fiap" and usuario == "admin":
    print("Acesso permitido!")
else:
    print("Senha ou usuario incorretos")


#Outro exemplo AND

